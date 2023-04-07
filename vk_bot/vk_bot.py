import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import get_course
from wiki import get_article
import Parsing
with open("Key.txt") as file:
    token = file.readline()

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        print(msg)
        user_id = event.user_id
        random_id = random.randint(1, 10**10) # <----
        if msg == "планеты":
            vk.messages.send(user_id=user_id, random_id=random_id, message = Parsing.planet(Parsing.urls[0]))
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
