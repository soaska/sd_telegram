from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_start_keyboard(sd_status: str) -> InlineKeyboardMarkup:
    keys = [
        InlineKeyboardButton(text=f"{sd_status} sd", callback_data="sd"),
        InlineKeyboardButton(text="opt", callback_data="opt"),
        InlineKeyboardButton(text="gen", callback_data="gen"),
        InlineKeyboardButton(text="skip", callback_data="skip"),
        InlineKeyboardButton(text="help", callback_data="help"),
    ]
    return InlineKeyboardMarkup(inline_keyboard=[keys])

def get_opt_keyboard() -> InlineKeyboardMarkup:
    keys = [
        InlineKeyboardButton(text="sttngs", callback_data="sttngs"),
        InlineKeyboardButton(text="scrpts", callback_data="scrpts"),
        InlineKeyboardButton(text="mdl", callback_data="mdl"),
        InlineKeyboardButton(text="smplr", callback_data="smplr"),
        InlineKeyboardButton(text="hr", callback_data="hr"),
        InlineKeyboardButton(text="prompt", callback_data="prompt"),
    ]
    return InlineKeyboardMarkup(inline_keyboard=[keys])

def get_scripts_keyboard() -> InlineKeyboardMarkup:
    keys = [
        InlineKeyboardButton(text="get_lora", callback_data="get_lora"),
        InlineKeyboardButton(text="rnd_mdl", callback_data="rnd_mdl"),
        InlineKeyboardButton(text="rnd_smp", callback_data="rnd_smp"),
        InlineKeyboardButton(text="inf", callback_data="inf"),
    ]
    return InlineKeyboardMarkup(inline_keyboard=[keys])

def get_settings_keyboard() -> InlineKeyboardMarkup:
    keys = [
        InlineKeyboardButton(text="change_param", callback_data="change_param"),
        InlineKeyboardButton(text="reset_param", callback_data="reset_param"),
        InlineKeyboardButton(text="fast_param", callback_data="fast_param"),
    ]
    return InlineKeyboardMarkup(inline_keyboard=[keys])

def get_fast_params_keyboard() -> InlineKeyboardMarkup:
    keys = [
        InlineKeyboardButton(text="comp", callback_data="fp_comp"),
        InlineKeyboardButton(text="mobile", callback_data="fp_mobile"),
        InlineKeyboardButton(text="no hr", callback_data="fp_no_hr"),
        InlineKeyboardButton(text="big", callback_data="fp_big"),
        InlineKeyboardButton(text="inc", callback_data="fp_inc"),
        InlineKeyboardButton(text="sdxl", callback_data="fp_sdxl"),
        InlineKeyboardButton(text="w↔h", callback_data="fp_wh"),
    ]
    return InlineKeyboardMarkup(inline_keyboard=[keys])

def get_yes_no_keyboard(name: str) -> InlineKeyboardMarkup:
    keys = [
        InlineKeyboardButton(text="✅", callback_data=f"yes_{name}"),
        InlineKeyboardButton(text="❌", callback_data=f"no_{name}")
    ]
    return InlineKeyboardMarkup(inline_keyboard=[keys])

def get_prompt_keyboard(chat_history: bool) -> InlineKeyboardMarkup:
    keys = [
        InlineKeyboardButton(text="get", callback_data="get"),
        InlineKeyboardButton(text="random", callback_data="random_prompt"),
        InlineKeyboardButton(text="lxc", callback_data="lxc_prompt"),
    ]
    if chat_history:
        keys.append(InlineKeyboardButton(text="json", callback_data="next"))
    return InlineKeyboardMarkup(inline_keyboard=[keys])

def get_prompt_from_json_keyboard() -> InlineKeyboardMarkup:
    keys = [
        InlineKeyboardButton(text="Next prompt", callback_data="next"),
        InlineKeyboardButton(text="Save", callback_data="save_prompt")
    ]
    return InlineKeyboardMarkup(inline_keyboard=[keys])

def get_change_param_keyboard(params: dict) -> InlineKeyboardMarkup:
    keys = []
    for key, value in params.items():
        keys.append([InlineKeyboardButton(text=f"{key}: {value}", callback_data=f"change_{key}")])
    return InlineKeyboardMarkup(inline_keyboard=keys)

def get_fast_param_keyboard(presets: dict) -> InlineKeyboardMarkup:
    keys = []
    for preset_name in presets.keys():
        keys.append(InlineKeyboardButton(text=preset_name, callback_data=f"preset_{preset_name}"))
    return InlineKeyboardMarkup(inline_keyboard=[keys])