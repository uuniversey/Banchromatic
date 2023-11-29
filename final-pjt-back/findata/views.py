from django.shortcuts import render
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingsProductsSerializer, SavingsOptionsSerializer, ExchangeRatesSerializer
from .models import DepositOptions, DepositProducts, SavingsProducts, SavingsOptions, ExchangeRates
from django.http import JsonResponse
import requests


# Create your views here.

# 예금 api db에 저장
@api_view(['GET'])
def save_data_deposit(request):
    api_key = settings.API_KEY_FIN
    url_deposit = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response_deposit = requests.get(url_deposit).json()
    deposit_info = response_deposit.get('result').get('baseList')
    for deposit in deposit_info:
        save_data = {
            'fin_prdt_cd' : deposit.get('fin_prdt_cd'),
            'kor_co_nm' : deposit.get('kor_co_nm'),
            'fin_prdt_nm' : deposit.get('fin_prdt_nm'),                 
            'etc_note' : deposit.get('etc_note'),                 
            'join_deny' : deposit.get('join_deny'),             
            'join_member' : deposit.get('join_member'),              
            'join_way' : deposit.get('join_way'),                  
            'spcl_cnd' : deposit.get('spcl_cnd'),
        }

        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    option_list = response_deposit.get('result').get("optionList")
    for ol in option_list:
        o_save_data = {
            'fin_prdt_cd' : ol.get('fin_prdt_cd'),
            'intr_rate_type_nm' : ol.get('intr_rate_type_nm'),
            'intr_rate' : ol.get('intr_rate'),                
            'intr_rate2' : ol.get('intr_rate2'),               
            'save_trm' : ol.get('save_trm'),                 
        }

        for data in o_save_data:
            if o_save_data[data] == None:
                o_save_data[data] = -1

        product = DepositProducts.objects.get(fin_prdt_cd = ol.get('fin_prdt_cd'))
        serializer = DepositOptionsSerializer(data=o_save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)

    return Response(response_deposit)


# 적금 api db에 저장
@api_view(['GET'])
def save_data_saving(request):
    api_key = settings.API_KEY_FIN
    url_saving = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response_saving = requests.get(url_saving).json()

    saving_info = response_saving.get('result').get('baseList')
    for saving in saving_info:
        save_data = {
            'fin_prdt_cd' : saving.get('fin_prdt_cd'),
            'kor_co_nm' : saving.get('kor_co_nm'),
            'fin_prdt_nm' : saving.get('fin_prdt_nm'),                 
            'etc_note' : saving.get('etc_note'),                 
            'join_deny' : saving.get('join_deny'),             
            'join_member' : saving.get('join_member'),              
            'join_way' : saving.get('join_way'),                  
            'spcl_cnd' : saving.get('spcl_cnd'),
        }

        serializer = SavingsProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    option_list = response_saving.get('result').get("optionList")
    for ol in option_list:
        o_save_data = {
            'fin_prdt_cd' : ol.get('fin_prdt_cd'),
            'intr_rate_type_nm' : ol.get('intr_rate_type_nm'),
            'intr_rate' : ol.get('intr_rate'),                
            'intr_rate2' : ol.get('intr_rate2'),               
            'save_trm' : ol.get('save_trm'),                 
        }

        for data in o_save_data:
            if o_save_data[data] == None:
                o_save_data[data] = -1

        product = SavingsProducts.objects.get(fin_prdt_cd = ol.get('fin_prdt_cd'))
        serializer = SavingsOptionsSerializer(data=o_save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)

    return Response(response_saving)


# front에서 db에 요청하는 함수
@api_view(['GET'])
def show_deposit_products(request):
    show_data = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(instance=show_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def show_deposit_options(request):
    show_data = DepositOptions.objects.all()
    serializer = DepositOptionsSerializer(instance=show_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def show_saving_products(request):
    show_data = SavingsProducts.objects.all()
    serializer = SavingsProductsSerializer(instance=show_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def show_saving_options(request):
    show_data = SavingsOptions.objects.all()
    serializer = SavingsOptionsSerializer(instance=show_data, many=True)
    return Response(serializer.data)


# 자동 갱신 하나 필요


# 외부 api를 db에 가져오는 함수
@api_view(['GET'])
def exchangerates(request):
    api_key = settings.API_KEY_EXRATE
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&data=AP01'
    
    response = requests.get(url).json()
    for data in response:
        isExist = ExchangeRates.objects.filter(cur_unit=data.get('cur_unit')).exists()

        if not isExist:
            save_data = {
                'cur_unit': data.get('cur_unit'),
                'cur_nm': data.get('cur_nm'),
                'ttb': data.get('ttb'),
                'tts': data.get('tts'),
                'deal_bas_r': data.get('deal_bas_r'),
                'bkpr': data.get('bkpr'),
                'yy_efee_r': data.get('yy_efee_r'),
                'ten_dd_efee_r': data.get('ten_dd_efee_r'),
                'kftc_deal_bas_r': data.get('kftc_deal_bas_r'),
                'kftc_bkpr': data.get('kftc_bkpr'),
                }
            
            serializer = ExchangeRatesSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        else:
            existing_record = ExchangeRates.objects.get(cur_unit=data.get('cur_unit'))
            existing_record.cur_nm = data.get('cur_nm')
            existing_record.ttb = data.get('ttb')
            existing_record.tts = data.get('tts')
            existing_record.deal_bas_r = data.get('deal_bas_r')
            existing_record.bkpr = data.get('bkpr')
            existing_record.yy_efee_r = data.get('yy_efee_r')
            existing_record.ten_dd_efee_r = data.get('ten_dd_efee_r')
            existing_record.kftc_deal_bas_r = data.get('kftc_deal_bas_r')
            existing_record.kftc_bkpr = data.get('kftc_bkpr')

            existing_record.save()
            

    return Response(url)


# 프론트에서 db에 요청하는 함수 
@api_view(['GET'])
def showexchangerates(request):
    show_data = ExchangeRates.objects.all()
    serializer = ExchangeRatesSerializer(instance=show_data, many=True)
    return Response(serializer.data)


# 프론트에서 detail정보를 가져오기 위해 db에 요청하는 함수 (예금)
@api_view(['GET'])
def detail_deposit(request, name):
    info = DepositProducts.objects.get(fin_prdt_cd=name)
    serializer = DepositProductsSerializer(info)
    return Response(serializer.data)


# 프론트에서 detail정보를 가져오기 위해 db에 요청하는 함수 (적금)
@api_view(['GET'])
def detail_savings(request, name):
    info = SavingsProducts.objects.get(fin_prdt_cd=name)
    serializer = SavingsProductsSerializer(info)
    return Response(serializer.data)


# 환전하는 함수
@api_view(['GET'])
def exchange_calc(request, name1, name2):
    before = ExchangeRates.objects.get(cur_nm=name1).deal_bas_r.replace(',', '')
    after = ExchangeRates.objects.get(cur_nm=name2).deal_bas_r.replace(',', '')
    exception = ['일본 옌', '인도네시아 루피아']
    result = float(before) / float(after)
    if name1 in exception:
        result /= 100
    elif name2 in exception:
        result *= 100
    
    return Response(result)