import webuiapi
import os
import asyncio
from config import SD_HOST, SD_PORT, SD_USERNAME, SD_PASSWORD, LORA_PATH

class SdApi:
    def __init__(self):
        self.api = webuiapi.WebUIApi(host=SD_HOST, port=SD_PORT)
        self.api.set_auth(SD_USERNAME, SD_PASSWORD)

    async def get_models(self):
        return await asyncio.to_thread(self.api.get_sd_models)

    async def get_samplers(self):
        return await asyncio.to_thread(self.api.get_samplers)

    async def get_schedulers(self):
        return await asyncio.to_thread(self.api.get_schedulers)

    async def get_hr_upscalers(self):
        return await asyncio.to_thread(lambda: [str(choice.value) for choice in webuiapi.HiResUpscaler])

    async def set_model(self, model):
        await asyncio.to_thread(self.api.util_set_model, model)
        await asyncio.to_thread(self.api.util_wait_for_ready)

    async def set_options(self, options):
        await asyncio.to_thread(self.api.set_options, options)

    async def txt2img(self, **kwargs):
        return await asyncio.to_thread(self.api.txt2img, **kwargs)

    async def get_progress(self):
        progress = await asyncio.to_thread(self.api.get_progress)
        return progress['progress']

    async def skip(self):
        return await asyncio.to_thread(self.api.skip)

    def get_loras(self):
        if not os.path.exists(LORA_PATH):
            return []
        file_list = os.listdir(LORA_PATH)
        lora_files = [
            file_name for file_name in file_list if file_name.endswith(".safetensors")
        ]
        return [file_name.replace(".safetensors", "") for file_name in lora_files]