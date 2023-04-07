import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import get_course
from wiki import get_article

# pip install beautifulsoup4
# pip install requests
# pip install vk-api
# pip uninstall vk_api

# pip install wikipedia
with open("Key.txt") as file:
    token = file.readline()

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)
#photo = upload.photo_messages("kit.jpg")

#Формат описания медиавложения: {type}{owner_id}_{media_id}
#attachment = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"
longpoll = VkLongPoll(vk_session)

#раньше -> while True

#сейчас:
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        print(msg)
        user_id = event.user_id
        random_id = random.randint(1, 10**10) # <----
        if msg == "привет":
            vk.messages.send(user_id=user_id, random_id=random_id, message = "Салам Уалейкум")
        elif msg == "-к":
            responce = f"{get_course('R01235')} рублей за доллар"
            vk.messages.send(user_id=user_id, random_id=random_id, message = responce)
        elif msg.startswith("-в"):
            article = msg[2:]
            responce = get_article(article=article)
            vk.messages.send(user_id=user_id, random_id=random_id, message = responce)
        else:
            responce = f"неизвестная команда"
            vk.messages.send(user_id=user_id, random_id=random_id, message = responce)
