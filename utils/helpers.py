import io
from PIL import Image
from aiogram import types

def pil_to_images(res, image_type="tg"):
    media_group = []
    images_all = res.images
    
    i = -1 if len(images_all) > 1 else 0
        
    for image in images_all:
        seed = str(res.info["all_seeds"][i])
        image_buffer = io.BytesIO()
        image.save(image_buffer, format="PNG")
        image_buffer.seek(0)

        if image_type == "tg":
            media_group.append(types.InputMediaPhoto(media=image_buffer, caption=seed))
        elif image_type == "real":
            media_group.append(
                types.InputMediaDocument(
                    media=types.InputFile(image_buffer, filename=seed + ".png"), caption=seed
                )
            )
        elif image_type == "thumbs":
            img = Image.open(image_buffer)
            width, height = img.size
            ratio = min(256 / width, 256 / height)
            new_size = (round(width * ratio), round(height * ratio))
            img = img.resize(new_size)
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format="PNG")
            img_byte_arr.seek(0)
            media_group.append(types.InputMediaPhoto(media=img_byte_arr, caption=seed))
        
        i += 1
            
    return media_group