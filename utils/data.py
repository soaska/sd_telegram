import json

class BotData:
    def __init__(self, prompts_file, presets_file):
        with open(prompts_file, 'r') as f:
            self.prompts = json.load(f)
        with open(presets_file, 'r') as f:
            self.presets = json.load(f)
        
        self.current_params = {
            "prompt": self.prompts.get("default", ""),
            "negative_prompt": self.prompts.get("negative_prompt", ""),
            "steps": 15,
            "sampler_name": "Euler a",
            "scheduler": "karras",
            "cfg_scale": 7,
            "width": 512,
            "height": 512,
            "seed": -1,
            "enable_hr": False,
            "denoising_strength": 0.7,
            "hr_upscaler": "None",
            "hr_second_pass_steps": 0,
            "restore_faces": False,
            "do_not_save_grid": True,
            "save_images": True,
        }
        
        self.user_settings = {
            "img_thumb": True,
            "img_tg": False,
            "img_real": True,
            "stop_sd": True,
            "sd_model_checkpoint": "",
            "use_prompt": True,
            "json_prompt": False,
            "just_gen": False,
            "send_vk": False,
        }
        self.sd_status = "❌"

    def get_params(self):
        return self.current_params

    def get_user_settings(self):
        return self.user_settings

    def update_params(self, new_params):
        self.current_params.update(new_params)

    def update_user_settings(self, new_settings):
        self.user_settings.update(new_settings)

    def reset_params(self):
        self.current_params = self.presets.get("default", {})

    def apply_preset(self, preset_name):
        preset = self.presets.get(preset_name)
        if preset:
            self.update_params(preset)

    def toggle_sd_status(self):
        if self.sd_status == "❌":
            self.sd_status = "✅"
        else:
            self.sd_status = "❌"
        return self.sd_status