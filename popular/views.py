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
            "id": 1,
            "name": "برجر.",
            "description": "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?",
            "price": 76,
            "stars": 76,
            "img": "https://images2.minutemediacdn.com/image/upload/c_crop,h_1126,w_2000,x_0,y_181/f_auto,q_auto,w_1100/v1554932288/shape/mentalfloss/12531-istock-637790866.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 2,
            "name": "فتوش.",
            "description": "Shanghai But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?.",
            "price": 76,
            "stars": 76,
            "img": "https://health.clevelandclinic.org/wp-content/uploads/sites/3/2016/10/foodJointPainRelief-142336977-770x533-1.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 3,
            "name": "كباب",
            "description": "Shanghai But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?.",
            "price": 76,
            "stars": 76,
            "img": "https://a.storyblok.com/f/62776/512x256/dd8a3a1d71/chicken-wide.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 4,
            "name": "كبسة",
            "description": "Shanghai But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?.",
            "price": 76,
            "stars": 76,
            "img": "https://health.clevelandclinic.org/wp-content/uploads/sites/3/2016/10/foodJointPainRelief-142336977-770x533-1.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 5,
            "name": "ملوخية",
            "description": "Shanghai But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?.",
            "price": 76,
            "stars": 76,
            "img": "https://a.storyblok.com/f/62776/512x256/dd8a3a1d71/chicken-wide.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 6,
            "name": "مفطح",
            "description": "Shanghai But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?.",
            "price": 76,
            "stars": 76,
            "img": "https://health.clevelandclinic.org/wp-content/uploads/sites/3/2016/10/foodJointPainRelief-142336977-770x533-1.jpg",
            "location": "China",
            "created_at": "2022-12-27 06:56:34",
            "updated_at": "2022-12-27 06:56:34",
            "type_id": 6
        },
        {
            "id": 7,
            "name": "مقلوبة",
            "description": "Shanghai But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?.",
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