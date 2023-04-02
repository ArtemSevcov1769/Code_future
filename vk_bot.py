import vk_api

with open("Key.txt") as file:
    token = file.readline()

vk = vk_api.VkApi(token=token)
while True:
    messages = vk.method('messages.getConversations', {'count' : 20, 'filter':'unanswered'})
    if messages['count'] >= 1:
        print(messages)
        user_id = messages['items'][0]['last_message']['from_id']
        message_text = messages['items'][0]['last_message']['text']
        vk.method('messages.send', {'user_id': user_id, 'random_id': 1, 'message': '1234'})