from django.db import models

# Create your models here.


# 정기예금
# 1. 상품
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)     # 금융 상품 코드
    kor_co_nm = models.TextField()                  # 금융 회사명
    fin_prdt_nm = models.TextField()                # 금융 상품명   
    etc_note = models.TextField()                   # 금융 상품 설명
    join_deny = models.IntegerField()               # 가입 제한(1: 제한x, 2: 서민제한, 3:일부제한)
    join_member = models.TextField()                # 가입 대상
    join_way = models.TextField()                   # 가입 방법
    spcl_cnd = models.TextField()                   # 우대조건


# 2. 옵션
class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)  # 외래 키
    fin_prdt_cd = models.TextField()                # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축 금리 유형명
    intr_rate = models.FloatField()                 # 저축 금리
    intr_rate2 = models.FloatField()                # 최고 우대 금리
    save_trm = models.IntegerField()                # 저축기간(개월)


# 적금
# 1. 상품
class SavingsProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)     # 금융 상품 코드
    kor_co_nm = models.TextField()                  # 금융 회사명
    fin_prdt_nm = models.TextField()                # 금융 상품명   
    etc_note = models.TextField()                   # 금융 상품 설명
    join_deny = models.IntegerField()               # 가입 제한(1: 제한x, 2: 서민제한, 3:일부제한)
    join_member = models.TextField()                # 가입 대상
    join_way = models.TextField()                   # 가입 방법
    spcl_cnd = models.TextField()                   # 우대조건


# 2. 옵션
class SavingsOptions(models.Model):
    product = models.ForeignKey(SavingsProducts, on_delete=models.CASCADE)  # 외래 키
    fin_prdt_cd = models.TextField()                # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축 금리 유형명
    intr_rate = models.FloatField()                 # 저축 금리
    intr_rate2 = models.FloatField()                # 최고 우대 금리
    save_trm = models.IntegerField()                # 저축기간(개월)


# 환율 정보
class ExchangeRates(models.Model):
    cur_unit = models.TextField()
    cur_nm = models.TextField()
    ttb = models.TextField()
    tts = models.TextField()
    deal_bas_r = models.TextField()
    bkpr = models.TextField()
    yy_efee_r = models.TextField()
    ten_dd_efee_r = models.TextField()
    kftc_deal_bas_r = models.TextField()
    kftc_bkpr = models.TextField()
