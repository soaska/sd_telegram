# This file contains the callback query handlers.
from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from keyboards.inline import get_start_keyboard, get_opt_keyboard, get_settings_keyboard, get_scripts_keyboard, get_prompt_keyboard, get_change_param_keyboard, get_fast_param_keyboard
from services.sd_api import SdApi
from services.scripts import Scripts
from utils.data import BotData
from utils.states import Form

router = Router()
sd_api = SdApi()

@router.callback_query(lambda c: c.data == "sd")
async def handle_sd_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the SD status toggle."""
    # This is a placeholder for the actual logic of starting/stopping SD
    # We will need to implement a more robust solution for managing the SD process
    new_status = bot_data.toggle_sd_status()
    await callback_query.message.edit_text(
        f"SD status toggled to {new_status}",
        reply_markup=get_start_keyboard(new_status)
    )

@router.callback_query(lambda c: c.data == "opt")
async def handle_opt_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'opt' callback."""
    await callback_query.message.edit_text(
        "Options",
        reply_markup=get_opt_keyboard()
    )

@router.callback_query(lambda c: c.data == "sttngs")
async def handle_sttngs_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'sttngs' callback."""
    await callback_query.message.edit_text(
        "Settings",
        reply_markup=get_settings_keyboard()
    )

@router.callback_query(lambda c: c.data == "scrpts")
async def handle_scrpts_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'scrpts' callback."""
    await callback_query.message.edit_text(
        "Scripts",
        reply_markup=get_scripts_keyboard()
    )

@router.callback_query(lambda c: c.data == "mdl")
async def handle_mdl_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'mdl' callback."""
    # Placeholder for model selection
    await callback_query.message.edit_text("Model selection placeholder")

@router.callback_query(lambda c: c.data == "smplr")
async def handle_smplr_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'smplr' callback."""
    # Placeholder for sampler selection
    await callback_query.message.edit_text("Sampler selection placeholder")

@router.callback_query(lambda c: c.data == "hr")
async def handle_hr_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'hr' callback."""
    # Placeholder for hr upscaler selection
    await callback_query.message.edit_text("HR upscaler selection placeholder")

@router.callback_query(lambda c: c.data == "prompt")
async def handle_prompt_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'prompt' callback."""
    await callback_query.message.edit_text(
        "Prompt options",
        reply_markup=get_prompt_keyboard(False) # Placeholder
    )

@router.callback_query(lambda c: c.data == "change_param")
async def handle_change_param_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'change_param' callback."""
    params = bot_data.get_params()
    await callback_query.message.edit_text(
        "Select a parameter to change:",
        reply_markup=get_change_param_keyboard(params)
    )

@router.callback_query(lambda c: c.data == "reset_param")
async def handle_reset_param_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'reset_param' callback."""
    bot_data.reset_params()
    await callback_query.message.edit_text(
        "Parameters have been reset to their default values.",
        reply_markup=get_settings_keyboard()
    )

@router.callback_query(lambda c: c.data.startswith("change_"))
async def handle_change_single_param_callback(callback_query: types.CallbackQuery, state: FSMContext):
    """Handles the callback for changing a single parameter."""
    param_to_change = callback_query.data.split("_")[1]
    await state.set_state(getattr(Form, param_to_change))
    await callback_query.message.edit_text(f"Please enter the new value for {param_to_change}:")

@router.callback_query(lambda c: c.data == "fast_param")
async def handle_fast_param_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'fast_param' callback."""
    presets = bot_data.presets
    await callback_query.message.edit_text(
        "Select a preset:",
        reply_markup=get_fast_param_keyboard(presets)
    )

@router.callback_query(lambda c: c.data.startswith("preset_"))
async def handle_preset_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the callback for applying a preset."""
    preset_name = callback_query.data.split("_")[1]
    bot_data.apply_preset(preset_name)
    await callback_query.message.edit_text(
        f"Preset '{preset_name}' has been applied.",
        reply_markup=get_settings_keyboard()
    )

@router.callback_query(lambda c: c.data == "gen")
async def handle_gen_callback(callback_query: types.CallbackQuery, scripts: Scripts):
    """Handles the 'gen' callback."""
    await callback_query.message.edit_text("Generating image...")
    await scripts.generate_image(callback_query.from_user.id)

@router.callback_query(lambda c: c.data == "skip")
async def handle_skip_callback(callback_query: types.CallbackQuery, sd_api: SdApi):
    """Handles the 'skip' callback."""
    await sd_api.skip()
    await callback_query.message.edit_text("Image generation skipped.")

@router.callback_query(lambda c: c.data == "get_lora")
async def handle_get_lora_callback(callback_query: types.CallbackQuery, sd_api: SdApi):
    """Handles the 'get_lora' callback."""
    loras = await sd_api.get_loras()
    if not loras:
        await callback_query.message.edit_text("No LORA files found.")
        return

    lora_list = "\n".join([f"`<lora:{name}:1>`" for name in loras])
    await callback_query.message.edit_text(lora_list, parse_mode="Markdown")

@router.callback_query(lambda c: c.data == "rnd_mdl")
async def handle_rnd_mdl_callback(callback_query: types.CallbackQuery, scripts: Scripts):
    """Handles the 'rnd_mdl' callback."""
    await callback_query.message.edit_text("Starting random model script...")
    await scripts.random_model_script(callback_query.from_user.id)

@router.callback_query(lambda c: c.data == "rnd_smp")
async def handle_rnd_smp_callback(callback_query: types.CallbackQuery, scripts: Scripts):
    """Handles the 'rnd_smp' callback."""
    await callback_query.message.edit_text("Starting random sampler script...")
    await scripts.random_sampler_script(callback_query.from_user.id)

@router.callback_query(lambda c: c.data == "inf")
async def handle_inf_callback(callback_query: types.CallbackQuery, scripts: Scripts):
    """Handles the 'inf' callback."""
    await callback_query.message.edit_text("Starting infinite generation script...")
    await scripts.infinite_script(callback_query.from_user.id)