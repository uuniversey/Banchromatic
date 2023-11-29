from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User
from findata.models import DepositProducts, SavingsProducts
from .serializers import CustomRegisterSerializer, UserSerializer
from findata.serializers import DepositProductsSerializer, SavingsProductsSerializer

# Create your views here.

# 프론트에서 유저 정보를 가져오기 위해 db에 요청하는 함수
@api_view(['GET'])
def profile(request, name):
    info = User.objects.get(username=name)
    serializer = CustomRegisterSerializer(info)
    return Response(serializer.data)


# 프로필을 수정하는 함수
@api_view(['GET', 'PUT'])
def profilechange(request, name):
    info = User.objects.get(username=name)
    
    if request.method == 'GET':
        serializer = CustomRegisterSerializer(info)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(info, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    

# 가입된 예금 정보를 가져오기 위해 db에 요청하는 함수
@api_view(['GET'])
def registered_deposit(request, name):
    user = User.objects.get(username=name)
    info_list = user.financial_products_deposit.all()
    serializer = DepositProductsSerializer(info_list, many=True)
    return Response(serializer.data)


# 가입된 적금 정보를 가져오기 위해 db에 요청하는 함수
@api_view(['GET'])
def registered_saving(request, name):
    user = User.objects.get(username=name)
    info_list = user.financial_products_saving.all()
    serializer = SavingsProductsSerializer(info_list, many=True)
    return Response(serializer.data)


# 예금 가입하는 함수
@api_view(['POST'])
def join_deposit(request, username):
    user = User.objects.get(username=username)
    financial_product = DepositProducts.objects.get(fin_prdt_cd=request.data.get('prdtcd'))
    user.financial_products_deposit.add(financial_product)
    return Response()


# 적금 가입 삭제하는 함수
@api_view(['DELETE'])
def delete_deposit(request, username):
    user = User.objects.get(username=username)
    financial_product = DepositProducts.objects.get(fin_prdt_cd=request.data.get('prdtcd'))
    user.financial_products_deposit.remove(financial_product)
    return Response()


# 예금 가입하는 함수
@api_view(['POST'])
def join_saving(request, username):
    user = User.objects.get(username=username)
    financial_product = SavingsProducts.objects.get(fin_prdt_cd=request.data.get('prdtcd'))
    user.financial_products_saving.add(financial_product)
    return Response()


# 적금 가입 삭제하는 함수
@api_view(['DELETE'])
def delete_saving(request, username):
    user = User.objects.get(username=username)
    financial_product = SavingsProducts.objects.get(fin_prdt_cd=request.data.get('prdtcd'))
    user.financial_products_saving.remove(financial_product)
    return Response()

