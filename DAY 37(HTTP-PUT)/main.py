from datetime import datetime
import requests

#PART - 1

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "shiwansh"
TOKEN =  "weopwopj230th23pgnowej"
ID = "graph"
header = {
    "X-USER-TOKEN" : TOKEN
}
date = datetime.today()
date = date.strftime("%Y%m%d")

# user_params ={
#     "token" : TOKEN,
#     "username" : USERNAME,
#     "agreeTermsOfService" : "yes",
#     "notMinor" : "yes"
# }

# r1 = requests.post(url=PIXELA_ENDPOINT,json=user_params)
# print(r1.status_code)
# print(r1.text)

#PART - 2

# GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#
# graph_params ={
#     "id" : ID,
#     "name" : "shiwansh",
#     "unit" : 'km',
#     "type" : "float",
#     "color" : "kuro"
# }

# r2 = requests.post(url=GRAPH_ENDPOINT,json=graph_params,headers=header)
# print(r2.text)

#PART - 3

#VALUE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}"
#
#
# VALUE_PARAMS = {
#     "date" : date,
#     "quantity" : "10.5",
# }
#
# r3 = requests.post(url=VALUE_ENDPOINT,json=VALUE_PARAMS,headers=header)
# print(r3.text)

#PART - 4(checking PUT)

PUT_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{date}"
PUT_PARAMS = {
    "quantity" : "8",
}

r4 = requests.put(url=PUT_ENDPOINT,json=PUT_PARAMS,headers=header)
print(r4.text)

#WE CAN ALSO USE REQUEST.DELETE TO DELETE A DATA
