import vk_api
from vk_api import VkUpload
from ok_api import OkApi, Upload
import requests
import os
from config import (
    VK_TOKEN,
    VK_ALBUM_ID,
    OK_ACCESS_TOKEN,
    OK_APPLICATION_KEY,
    OK_APPLICATION_SECRET_KEY,
    OK_GROUP_ID,
    API_BOT_TOKEN,
)

class SocialApi:
    def __init__(self, bot):
        self.bot = bot
        self.vk_session = vk_api.VkApi(token=VK_TOKEN)
        self.vk_upload = VkUpload(self.vk_session)
        self.ok_api = OkApi(
            access_token=OK_ACCESS_TOKEN,
            application_key=OK_APPLICATION_KEY,
            application_secret_key=OK_APPLICATION_SECRET_KEY,
        )
        self.ok_upload = Upload(self.ok_api)

    def upload_to_vk(self, file_path, caption):
        try:
            self.vk_upload.photo(
                photos=file_path,
                album_id=VK_ALBUM_ID,
                caption=caption
            )
            return True, None
        except Exception as e:
            return False, str(e)

    def upload_to_ok(self, file_path, caption):
        try:
            upload_response = self.ok_upload.photo(photos=[file_path], album=OK_GROUP_ID)
            for photo_id in upload_response['photos']:
                token = upload_response['photos'][photo_id]['token']
                self.ok_api.photosV2.commit(photo_id=photo_id, token=token, comment=caption)
            return True, None
        except Exception as e:
            return False, str(e)

    async def download_file(self, file_id):
        file_obj = await self.bot.get_file(file_id)
        file_url = f'https://api.telegram.org/file/bot{API_BOT_TOKEN}/{file_obj.file_path}'

        temp_file_path = 'temp.png'
        with open(temp_file_path, 'wb') as file:
            file.write(requests.get(file_url).content)
            
        return temp_file_path

    def cleanup_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)