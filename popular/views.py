from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import json

def index(request):

    json_data = """{
    "total_size": 0,
    "type_id": 35,
    "offset": 76,
    "products": [
        {
            "id": 76,
            "name": "Shanghai jguk.",
            "description": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "price": 76,
            "stars": 76,
            "img": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 76,
            "name": "Shanghai jguk.",
            "description": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "price": 76,
            "stars": 76,
            "img": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 76,
            "name": "Shanghai jguk.",
            "description": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "price": 76,
            "stars": 76,
            "img": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        }
    ]
}"""


    data = json.loads(json_data)
    
    return JsonResponse(data)