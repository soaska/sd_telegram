# This file contains the command handlers for regular users.
from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboards.inline import get_start_keyboard
from filters.admin import IsAdmin
from utils.data import BotData
from utils.states import Form
from services.scripts import Scripts

router = Router()

@router.message(Command(commands=["start", "help"]), IsAdmin())
async def cmd_start(message: types.Message, bot_data: BotData):
    """Handles the /start and /help commands."""
    txt = "This is a bot for locally running SD\n/start /opt /gen /skip /stop /help"
    await message.answer(txt, reply_markup=get_start_keyboard(bot_data.sd_status))

@router.message(Command(commands=["gen_custom"]), IsAdmin())
async def cmd_gen_custom(message: types.Message, state: FSMContext):
    """Starts the custom image generation process."""
    await state.set_state(Form.prompt)
    await message.answer("Please enter the prompt:")

@router.message(Form.prompt, IsAdmin())
async def process_prompt(message: types.Message, state: FSMContext):
    """Processes the prompt and asks for the number of steps."""
    await state.update_data(prompt=message.text)
    await state.set_state(Form.steps)
    await message.answer("Please enter the number of steps:")

@router.message(Form.steps, IsAdmin())
async def process_steps(message: types.Message, state: FSMContext, bot_data: BotData, scripts: Scripts):
    """Processes the number of steps and starts the image generation."""
    try:
        steps = int(message.text)
        if steps <= 0:
            await message.answer("Please enter a positive number for steps.")
            return
        await state.update_data(steps=steps)
        data = await state.get_data()
        bot_data.update_params(data)
        await state.clear()
    except ValueError:
        await message.answer("Invalid input. Please enter a number for steps.")
    await message.answer("Generating image with custom settings...")
    await scripts.generate_image(message.from_user.id)

@router.message(IsAdmin())
async def handle_user_input(message: types.Message, state: FSMContext, bot_data: BotData):
    """Handles user input when in a state."""
    current_state = await state.get_state()
    if current_state:
        param_to_change = current_state.split(":")[1]
        new_value = message.text
        bot_data.update_params({param_to_change: new_value})
        await state.clear()
        await message.answer(f"Parameter {param_to_change} has been updated to {new_value}.")
    else:
        # Handle regular text messages here if needed
        pass