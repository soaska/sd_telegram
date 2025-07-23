# This file contains the callback query handlers.
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from keyboards.inline import (
    get_start_keyboard, get_opt_keyboard, get_settings_keyboard,
    get_scripts_keyboard, get_prompt_keyboard, get_change_param_keyboard,
    get_fast_param_keyboard
)
from services.sd_api import SdApi
from services.scripts import Scripts
from utils.data import BotData
from utils.states import Form

router = Router()
sd_api = SdApi()

@router.callback_query(F.data == "start")
async def handle_start_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'start' (back) callback."""
    await callback_query.message.edit_text(
        "Welcome to the Stable Diffusion bot! Use the buttons below to get started.",
        reply_markup=get_start_keyboard(bot_data.sd_status)
    )

@router.callback_query(F.data == "help")
async def handle_help_callback(callback_query: types.CallbackQuery):
    """Handles the 'help' callback."""
    txt = (
        "Here's a quick guide to the bot's commands:\n\n"
        "<b>Commands:</b>\n"
        "/start - Welcome message and main menu\n"
        "/help - This help message\n"
        "/gen - Generate an image with the current settings\n"
        "/gen_custom - Start a guided process to generate an image with custom settings\n"
        "/skip - Skip the current image generation\n"
        "/stop - Stop a running script (like infinite generation)\n\n"
        "<b>Main Menu Buttons:</b>\n"
        "<b>💡 SD</b> - Toggle the Stable Diffusion process on/off\n"
        "<b>⚙️ Options</b> - Open the options menu to change settings\n"
        "<b>🎨 Generate</b> - Generate an image\n"
        "<b>⏭️ Skip</b> - Skip the current generation\n"
        "<b>❓ Help</b> - Show this help message again"
    )
    await callback_query.message.edit_text(txt, parse_mode="HTML", reply_markup=get_start_keyboard("on")) # Assuming sd_status is 'on'

@router.callback_query(F.data == "sd")
async def handle_sd_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the SD status toggle."""
    new_status = bot_data.toggle_sd_status()
    await callback_query.message.edit_text(
        f"💡 Stable Diffusion is now {new_status}.",
        reply_markup=get_start_keyboard(new_status)
    )

@router.callback_query(F.data == "opt")
async def handle_opt_callback(callback_query: types.CallbackQuery):
    """Handles the 'opt' callback."""
    await callback_query.message.edit_text(
        "⚙️ Here you can configure the bot's settings and scripts.",
        reply_markup=get_opt_keyboard()
    )

@router.callback_query(F.data == "sttngs")
async def handle_sttngs_callback(callback_query: types.CallbackQuery):
    """Handles the 'sttngs' callback."""
    await callback_query.message.edit_text(
        "⚙️ Here you can change parameters, reset them to default, or use fast presets.",
        reply_markup=get_settings_keyboard()
    )

@router.callback_query(F.data == "scrpts")
async def handle_scrpts_callback(callback_query: types.CallbackQuery):
    """Handles the 'scrpts' callback."""
    await callback_query.message.edit_text(
        "📜 Here you can run various scripts.",
        reply_markup=get_scripts_keyboard()
    )

@router.callback_query(F.data == "mdl")
async def handle_mdl_callback(callback_query: types.CallbackQuery):
    """Handles the 'mdl' callback."""
    await callback_query.answer("This feature is not yet implemented.", show_alert=True)

@router.callback_query(F.data == "smplr")
async def handle_smplr_callback(callback_query: types.CallbackQuery):
    """Handles the 'smplr' callback."""
    await callback_query.answer("This feature is not yet implemented.", show_alert=True)

@router.callback_query(F.data == "hr")
async def handle_hr_callback(callback_query: types.CallbackQuery):
    """Handles the 'hr' callback."""
    await callback_query.answer("This feature is not yet implemented.", show_alert=True)

@router.callback_query(F.data == "prompt")
async def handle_prompt_callback(callback_query: types.CallbackQuery):
    """Handles the 'prompt' callback."""
    await callback_query.message.edit_text(
        "📝 Here you can manage your prompts.",
        reply_markup=get_prompt_keyboard(False)  # Placeholder
    )

@router.callback_query(F.data == "change_param")
async def handle_change_param_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'change_param' callback."""
    params = bot_data.get_params()
    await callback_query.message.edit_text(
        "✏️ Select a parameter to change:",
        reply_markup=get_change_param_keyboard(params)
    )

@router.callback_query(F.data == "reset_param")
async def handle_reset_param_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'reset_param' callback."""
    bot_data.reset_params()
    await callback_query.answer("Parameters have been reset to their default values.", show_alert=True)
    await callback_query.message.edit_text(
        "⚙️ Settings",
        reply_markup=get_settings_keyboard()
    )

@router.callback_query(F.data.startswith("change_"))
async def handle_change_single_param_callback(callback_query: types.CallbackQuery, state: FSMContext):
    """Handles the callback for changing a single parameter."""
    param_to_change = callback_query.data.split("_")[1]
    await state.set_state(getattr(Form, param_to_change))
    await callback_query.message.edit_text(f"✏️ Please enter the new value for {param_to_change}:")

@router.callback_query(F.data == "fast_param")
async def handle_fast_param_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the 'fast_param' callback."""
    presets = bot_data.presets
    await callback_query.message.edit_text(
        "⚡ Select a preset:",
        reply_markup=get_fast_param_keyboard(presets)
    )

@router.callback_query(F.data.startswith("preset_"))
async def handle_preset_callback(callback_query: types.CallbackQuery, bot_data: BotData):
    """Handles the callback for applying a preset."""
    preset_name = callback_query.data.split("_")[1]
    bot_data.apply_preset(preset_name)
    await callback_query.answer(f"Preset '{preset_name}' has been applied.", show_alert=True)
    await callback_query.message.edit_text(
        "⚙️ Settings",
        reply_markup=get_settings_keyboard()
    )

@router.callback_query(F.data == "gen")
async def handle_gen_callback(callback_query: types.CallbackQuery, scripts: Scripts):
    """Handles the 'gen' callback."""
    await callback_query.message.edit_text("🎨 Generating image...")
    await scripts.generate_image(callback_query.from_user.id)

@router.callback_query(F.data == "skip")
async def handle_skip_callback(callback_query: types.CallbackQuery, sd_api: SdApi):
    """Handles the 'skip' callback."""
    await sd_api.skip()
    await callback_query.answer("Image generation skipped.", show_alert=True)

@router.callback_query(F.data == "get_lora")
async def handle_get_lora_callback(callback_query: types.CallbackQuery, sd_api: SdApi):
    """Handles the 'get_lora' callback."""
    loras = await sd_api.get_loras()
    if not loras:
        await callback_query.answer("No LORA files found.", show_alert=True)
        return

    lora_list = "\n".join([f"`<lora:{name}:1>`" for name in loras])
    await callback_query.message.edit_text(f"✨ Available LORAs:\n\n{lora_list}", parse_mode="Markdown")

@router.callback_query(F.data == "rnd_mdl")
async def handle_rnd_mdl_callback(callback_query: types.CallbackQuery, scripts: Scripts):
    """Handles the 'rnd_mdl' callback."""
    await callback_query.message.edit_text("🎲 Starting random model script...")
    await scripts.random_model_script(callback_query.from_user.id)

@router.callback_query(F.data == "rnd_smp")
async def handle_rnd_smp_callback(callback_query: types.CallbackQuery, scripts: Scripts):
    """Handles the 'rnd_smp' callback."""
    await callback_query.message.edit_text("🎲 Starting random sampler script...")
    await scripts.random_sampler_script(callback_query.from_user.id)

@router.callback_query(F.data == "inf")
async def handle_inf_callback(callback_query: types.CallbackQuery, scripts: Scripts):
    """Handles the 'inf' callback."""
    await callback_query.message.edit_text("♾️ Starting infinite generation script...")
    await scripts.infinite_script(callback_query.from_user.id)