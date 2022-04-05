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
            "name": "برجر.",
            "description": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "price": 76,
            "stars": 76,
            "img": "https://images2.minutemediacdn.com/image/upload/c_crop,h_1126,w_2000,x_0,y_181/f_auto,q_auto,w_1100/v1554932288/shape/mentalfloss/12531-istock-637790866.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 76,
            "name": "فتوش.",
            "description": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "price": 76,
            "stars": 76,
            "img": "https://health.clevelandclinic.org/wp-content/uploads/sites/3/2016/10/foodJointPainRelief-142336977-770x533-1.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 76,
            "name": "كباب",
            "description": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "price": 76,
            "stars": 76,
            "img": "https://a.storyblok.com/f/62776/512x256/dd8a3a1d71/chicken-wide.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 76,
            "name": "كبسة",
            "description": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "price": 76,
            "stars": 76,
            "img": "https://health.clevelandclinic.org/wp-content/uploads/sites/3/2016/10/foodJointPainRelief-142336977-770x533-1.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 76,
            "name": "ملوخية",
            "description": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "price": 76,
            "stars": 76,
            "img": "https://a.storyblok.com/f/62776/512x256/dd8a3a1d71/chicken-wide.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 76,
            "name": "مفطح",
            "description": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "price": 76,
            "stars": 76,
            "img": "https://health.clevelandclinic.org/wp-content/uploads/sites/3/2016/10/foodJointPainRelief-142336977-770x533-1.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 76,
            "name": "مقلوبة",
            "description": "Shanghai jugikgig7ppppppppppppppppppppppppppppppppguk.",
            "price": 76,
            "stars": 76,
            "img": "https://www.wbcsd.org/var/site/storage/images/media/images/fresh_pa/80809-2-eng-GB/FRESH_PA_i1140.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        }

    ]
}"""


    data = json.loads(json_data)
    
    return JsonResponse(data)