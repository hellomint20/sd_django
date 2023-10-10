from rest_framework.response import Response
from rest_framework.decorators import api_view

from spring_test import bank_analysis

gbc = bank_analysis.init()

@api_view(['GET'])
def test(req):
    print("test 연동")
    print( req.GET )
    return Response({ "key" : "success" } )

@api_view(['GET'])
def bank(req):
    gbc = bank_analysis.init()
    print("bank 연동")
    print( req.GET )
    #'age' ,'duration', 'campaign', 'pdays', 'previous'
    result = gbc.predict([[
        req.GET['age'] , req.GET['duration'],req.GET['campaign'], 
         req.GET['pdays'], req.GET['previous']
    ]])
    print( "result : ", result )

    return Response({ "key" :  result[0] } )