import requests

url = "https://swapi.dev/api/"

response = requests.get(url).json()
planet_api = response.get("planets")
def planet(url):
    for i in range(1, 6):
        return requests.get(url + "/" + str(i)).json()

# def starships(url):
#     sp = []
#     for i in range(1, 10):
#         response = requests.get(url + "/" + str(i)).json()
#         print(response)
#         print(response.get("name"))
#         max_sp = (response.get("max_atmosphering_speed"))
#         print(max_sp)
#         if max_sp != "None" or max_sp != "unknow":
#             sp.append(max_sp)
#     max_number = max(sp)
#     print("Наибольшее число:", max_number)
#
#
#     # print(response["name"])
#
# # people(people_api)
starships(starships_api)
