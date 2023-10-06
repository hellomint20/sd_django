from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def test(req):
    print("test 연동")
    print(req.GET)
    print(req.GET['name'])
    return Response({"key" : "success"})

@api_view(['GET'])
def bank(req):
    print("bank 연동")
    print(req.GET)
    
    return Response({"key" : "success"})
