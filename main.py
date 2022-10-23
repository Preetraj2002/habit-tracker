import requests
from datetime import date as dt
import os

today=dt.today()


USERNAME=os.environ["PIXELA_USERNAME"]

TOKEN=os.environ["PIXELA_TOKEN"]

pixela_endpoint = "https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

id=os.environ["PIXELA_ID"]

graph_config={
    "id":id,
    "name":"trackmyreading",
    "unit":"pages",
    "type":"int",
    "color":"ajisai"     #care names of color are in japanese
}

headers={
    "X-USER-TOKEN":TOKEN
}



def init_user():
    response = requests.post(url=pixela_endpoint,json=user_params)
    print(response.text)


# Already created a graph so no need to execute this code
def create_graph():
    response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
    print(response.text)




def post_pixel(quan):
    pixel_config={
        "date":today.strftime("%Y%m%d"),
        "quantity":quan,
    }
    response=requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{id}", json=pixel_config, headers=headers)
    print(response.text)

def update_pixel(quan):

    update_config={
        "quantity":quan
    }
    response=requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{id}/{today.strftime('%Y%m%d')}",json=update_config,headers=headers)
    print(response.text)

def delete_pixel():
    response=requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{id}/{today.strftime('%Y%m%d')}",headers=headers)
    print(response.text)


# Already created user with these credentials so no need to execute this part
# init_user()

# Already created a graph so no need to execute this code
# create_graph()

pages=input("How many pages you read today? ")

post_pixel(pages)

update_pages=input("Update the number of pages (-1 for NO UPDATE) ")
if update_pages != "-1":
    update_pixel(update_pages)
# update_pixel("1000")

choice=int(input("Do you want to delete today's pixel (-1 for NO DELETION) "))
if choice!=-1:
    delete_pixel()                   #deletes today's pixel