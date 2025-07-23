from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_start_keyboard(sd_status: str) -> "InlineKeyboardMarkup":
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text=f"💡 SD {sd_status}", callback_data="sd"),
        InlineKeyboardButton(text="⚙️ Options", callback_data="opt"),
    )
    builder.row(
        InlineKeyboardButton(text="🎨 Generate", callback_data="gen"),
        InlineKeyboardButton(text="⏭️ Skip", callback_data="skip"),
        InlineKeyboardButton(text="❓ Help", callback_data="help"),
    )
    return builder.as_markup()

def get_opt_keyboard() -> "InlineKeyboardMarkup":
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⚙️ Settings", callback_data="sttngs"),
        InlineKeyboardButton(text="📜 Scripts", callback_data="scrpts"),
    )
    builder.row(
        InlineKeyboardButton(text="🤖 Model", callback_data="mdl"),
        InlineKeyboardButton(text="🖌️ Sampler", callback_data="smplr"),
        InlineKeyboardButton(text="🖼️ HR Upscaler", callback_data="hr"),
    )
    builder.row(InlineKeyboardButton(text="📝 Prompt", callback_data="prompt"))
    builder.row(InlineKeyboardButton(text="⬅️ Back", callback_data="start"))
    return builder.as_markup()

def get_scripts_keyboard() -> "InlineKeyboardMarkup":
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="✨ Get LORAs", callback_data="get_lora"),
        InlineKeyboardButton(text="🎲 Random Model", callback_data="rnd_mdl"),
    )
    builder.row(
        InlineKeyboardButton(text="🎲 Random Sampler", callback_data="rnd_smp"),
        InlineKeyboardButton(text="♾️ Infinite Generation", callback_data="inf"),
    )
    builder.row(InlineKeyboardButton(text="⬅️ Back", callback_data="opt"))
    return builder.as_markup()

def get_settings_keyboard() -> "InlineKeyboardMarkup":
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="✏️ Change Parameter", callback_data="change_param"),
        InlineKeyboardButton(text="🗑️ Reset Parameters", callback_data="reset_param"),
    )
    builder.row(InlineKeyboardButton(text="⚡ Fast Presets", callback_data="fast_param"))
    builder.row(InlineKeyboardButton(text="⬅️ Back", callback_data="opt"))
    return builder.as_markup()

def get_fast_params_keyboard() -> "InlineKeyboardMarkup":
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="💻 Computer", callback_data="fp_comp"),
        InlineKeyboardButton(text="📱 Mobile", callback_data="fp_mobile"),
        InlineKeyboardButton(text="🚫 No HR", callback_data="fp_no_hr"),
    )
    builder.row(
        InlineKeyboardButton(text="🖼️ Big Image", callback_data="fp_big"),
        InlineKeyboardButton(text="🔄 Increase Size", callback_data="fp_inc"),
        InlineKeyboardButton(text="🔥 SDXL", callback_data="fp_sdxl"),
    )
    builder.row(InlineKeyboardButton(text="↔️ W↔H", callback_data="fp_wh"))
    builder.row(InlineKeyboardButton(text="⬅️ Back", callback_data="sttngs"))
    return builder.as_markup()

def get_yes_no_keyboard(name: str) -> "InlineKeyboardMarkup":
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="✅ Yes", callback_data=f"yes_{name}"),
        InlineKeyboardButton(text="❌ No", callback_data=f"no_{name}")
    )
    return builder.as_markup()

def get_prompt_keyboard(chat_history: bool) -> "InlineKeyboardMarkup":
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="📥 Get Current", callback_data="get"),
        InlineKeyboardButton(text="🎲 Random", callback_data="random_prompt"),
        InlineKeyboardButton(text="✍️ Lexica", callback_data="lxc_prompt"),
    )
    if chat_history:
        builder.add(InlineKeyboardButton(text="📜 From History", callback_data="next"))
    builder.row(InlineKeyboardButton(text="⬅️ Back", callback_data="opt"))
    return builder.as_markup()

def get_prompt_from_json_keyboard() -> "InlineKeyboardMarkup":
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="▶️ Next", callback_data="next"),
        InlineKeyboardButton(text="💾 Save", callback_data="save_prompt")
    )
    builder.row(InlineKeyboardButton(text="⬅️ Back", callback_data="prompt"))
    return builder.as_markup()

def get_change_param_keyboard(params: dict) -> "InlineKeyboardMarkup":
    builder = InlineKeyboardBuilder()
    for key, value in params.items():
        builder.row(InlineKeyboardButton(text=f"{key}: {value}", callback_data=f"change_{key}"))
    builder.row(InlineKeyboardButton(text="⬅️ Back", callback_data="sttngs"))
    return builder.as_markup()

def get_fast_param_keyboard(presets: dict) -> "InlineKeyboardMarkup":
    builder = InlineKeyboardBuilder()
    for preset_name in presets.keys():
        builder.add(InlineKeyboardButton(text=preset_name, callback_data=f"preset_{preset_name}"))
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="⬅️ Back", callback_data="sttngs"))
    return builder.as_markup()