import random
import asyncio
from services.sd_api import SdApi
from utils.data import BotData
from utils.helpers import pil_to_images

class Scripts:
    def __init__(self, bot, sd_api: SdApi, bot_data: BotData):
        self.bot = bot
        self.sd_api = sd_api
        self.bot_data = bot_data
        self.running_tasks = {}

    async def generate_image(self, chat_id):
        params = self.bot_data.get_params()
        user_settings = self.bot_data.get_user_settings()

        try:
            # Send a message to show the progress
            progress_message = await self.bot.send_message(chat_id, "Generation started...")

            # Start the generation
            res = await self.sd_api.txt2img(**params)

            # Update the progress
            while await self.sd_api.get_progress() < 1:
                progress = await self.sd_api.get_progress() * 100
                await self.bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=progress_message.message_id,
                    text=f"Generation in progress: {progress:.2f}%"
                )
                await asyncio.sleep(1)

            # Delete the progress message
            await self.bot.delete_message(chat_id=chat_id, message_id=progress_message.message_id)
            
            if user_settings.get("img_thumb"):
                await self.bot.send_media_group(chat_id=chat_id, media=pil_to_images(res, "thumbs"))
            if user_settings.get("img_tg"):
                await self.bot.send_media_group(chat_id=chat_id, media=pil_to_images(res, "tg"))
            if user_settings.get("img_real"):
                await self.bot.send_media_group(chat_id=chat_id, media=pil_to_images(res, "real"))

            await self.bot.send_message(chat_id, f"Seed: {res.info['all_seeds'][0]}")
        except Exception as e:
            await self.bot.send_message(chat_id, f"An error occurred: {e}")

    async def random_model_script(self, chat_id):
        task = asyncio.create_task(self._random_model_script(chat_id))
        self.running_tasks[chat_id] = task

    async def _random_model_script(self, chat_id):
        try:
            models = await self.sd_api.get_models()
            random.shuffle(models)

            for model in models:
                await self.sd_api.set_model(model['model_name'])
                await self.generate_image(chat_id)
        except asyncio.CancelledError:
            await self.bot.send_message(chat_id, "Random model script stopped.")
        finally:
            if chat_id in self.running_tasks:
                del self.running_tasks[chat_id]

    async def random_sampler_script(self, chat_id):
        task = asyncio.create_task(self._random_sampler_script(chat_id))
        self.running_tasks[chat_id] = task

    async def _random_sampler_script(self, chat_id):
        try:
            samplers = await self.sd_api.get_samplers()
            random.shuffle(samplers)

            for sampler in samplers:
                self.bot_data.update_params({"sampler_name": sampler['name']})
                await self.generate_image(chat_id)
        except asyncio.CancelledError:
            await self.bot.send_message(chat_id, "Random sampler script stopped.")
        finally:
            if chat_id in self.running_tasks:
                del self.running_tasks[chat_id]

    async def infinite_script(self, chat_id):
        task = asyncio.create_task(self._infinite_script(chat_id))
        self.running_tasks[chat_id] = task

    async def _infinite_script(self, chat_id):
        try:
            while True:
                # This is a placeholder for the complex prompt generation logic.
                # We will implement a more robust solution later.
                prompt = "a beautiful landscape"
                
                params = {
                    "prompt": prompt,
                    "cfg_scale": round(random.uniform(4.7, 15), 1),
                    "steps": round(random.uniform(10, 80)),
                    "width": random.randrange(512, 1601, 64),
                    "height": random.randrange(512, 1601, 64),
                }
                
                while params["width"] * params["height"] > 1000000:
                    params["width"] = random.randrange(512, 1601, 64)
                    params["height"] = random.randrange(512, 1601, 64)

                self.bot_data.update_params(params)
                await self.generate_image(chat_id)
        except asyncio.CancelledError:
            await self.bot.send_message(chat_id, "Infinite generation script stopped.")
        finally:
            if chat_id in self.running_tasks:
                del self.running_tasks[chat_id]

    async def stop_script(self, chat_id):
        if chat_id in self.running_tasks:
            self.running_tasks[chat_id].cancel()
            return True
        return False