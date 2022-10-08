import requests
import datetime as dt

USERNAME = "arpita2803"
TOKEN = "3R+0oieZ$#i3GM8"
GRAPH_ID = "graph1"
pixela_url = "https://pixe.la/v1/users"
pixela_config = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_url, json=pixela_config)
# print(response.text)

graph_url = f"{pixela_url}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "meditation tracker",
    "unit": "Min",
    "type": "int",
    "color": "shibafu",
}
header = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_url, json=graph_config, headers=header)
# print(response.text)

target_graph_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}"
current_date = dt.datetime.today()
formatted_date = current_date.strftime("%Y%m%d")
pixel_update_config = {
    "date": formatted_date,
    "quantity": "30",
}

# response = requests.post(url=target_graph_url, json=pixel_update_config, headers=header)
# print(response.text)

update_date = (current_date - dt.timedelta(days=1)).strftime("%Y%m%d")
pixel_update_url = f"{target_graph_url}/{update_date}"
graph_update_config = {
    "quantity": "15",
}

# response = requests.put(url=pixel_update_url, json=graph_update_config, headers=header)
# print(response.text)

pixel_delete_url = f"{target_graph_url}/{update_date}"

response = requests.delete(url=pixel_delete_url, headers=header)
print(response.text)
