<template>
  <div class="rec_box">
    <div class="recc_box">
    <div class="title">📌 금융 상품 추천</div>
    <!-- 상품 목록 있을 때 -->
    <div class="rec_box1" v-if="nameList.length > 0">
      <div class="cal1">
        <div class="s_title"><strong>항목을 선택해주세요</strong></div>

        <!-- 추천 데이터 받는 곳 -->
        <p class="bank_name">은행명</p>
        <select class="form-select cal_s" v-model="bank">
          <option selected>은행 선택</option>
          <option value="국민은행">국민은행</option>
          <option value="광주은행">광주은행</option>
          <option value="경남은행">경남은행</option>
          <option value="농협은행주식회사">농협은행주식회사</option>
          <option value="대구은행">대구은행</option>
          <option value="부산은행">부산은행</option>
          <option value="수협은행">수협은행</option>
          <option value="신한은행">신한은행</option>
          <option value="우리은행">우리은행</option>
          <option value="전북은행">전북은행</option>
          <option value="주식회사 케이뱅크">주식회사 케이뱅크</option>
          <option value="주식회사 카카오뱅크">주식회사 카카오뱅크</option>
          <option value="중소기업은행">중소기업은행</option>
          <option value="제주은행">제주은행</option>
          <option value="토스뱅크 주식회사">토스뱅크 주식회사</option>
          <option value="하나은행">하나은행</option>
          <option value="한국산업은행">한국산업은행</option>
          <option value="한국스탠다드차타드은행">한국스탠다드차타드은행</option>
        </select>

        <p class="period">저축 기간</p>
        <select class="form-select" v-model="period">
          <option selected>기간 선택</option>
          <option> 6개월 </option>
          <option> 12개월 </option>
          <option> 24개월 </option>
          <option> 36개월 </option>
        </select>

        <p class="month">한달 저축 금액</p>
        <select class="form-select" v-model="cost">
          <option selected>금액 선택</option>
          <option>10만원 이하</option>
          <option>30만원 이하</option>
          <option>50만원 이하</option>
          <option>100만원 이하</option>
          <option>200만원 이하</option>
          <option>500만원 이하</option>
          <option>500만원 초과</option>
        </select>

        <button class="btn btn-primary search_btn" @click="getData(bank, period.slice(0, -2))">추천받기</button>
      </div>

      <div class="cal1_2">
        <div class="cal_e">
          <h4><strong>추천 상품 목록</strong></h4>
          <p class="my-4" v-for="elem in nameList"> - {{ elem }}</p>
        </div>

        <div class="cal_e">
          <h4><strong>베스트 상품</strong></h4>
          <p class="my-4">- {{ recommend }}</p>
        </div>

        <div class="cal_e">
          <h4><strong>베스트 상품의 이율</strong></h4>
          <p class="my-4">- {{ recommendIntr }}%</p>
        </div>

      </div>
    </div>

    <!-- 상품 목록 없을 때 -->
    <div class="rec_box2" v-else>
      <div class="cal2">
        <div class="s_title"><strong>항목을 선택해주세요</strong></div>

        <!-- 추천 데이터 받는 곳 -->
        <p class="bank_name">은행명</p>
        <select class="form-select cal_s" v-model="bank">
          <option selected>은행 선택</option>
          <option value="국민은행">국민은행</option>
          <option value="광주은행">광주은행</option>
          <option value="경남은행">경남은행</option>
          <option value="농협은행주식회사">농협은행주식회사</option>
          <option value="대구은행">대구은행</option>
          <option value="부산은행">부산은행</option>
          <option value="수협은행">수협은행</option>
          <option value="신한은행">신한은행</option>
          <option value="우리은행">우리은행</option>
          <option value="전북은행">전북은행</option>
          <option value="주식회사 케이뱅크">주식회사 케이뱅크</option>
          <option value="주식회사 카카오뱅크">주식회사 카카오뱅크</option>
          <option value="중소기업은행">중소기업은행</option>
          <option value="제주은행">제주은행</option>
          <option value="토스뱅크 주식회사">토스뱅크 주식회사</option>
          <option value="하나은행">하나은행</option>
          <option value="한국산업은행">한국산업은행</option>
          <option value="한국스탠다드차타드은행">한국스탠다드차타드은행</option>
        </select>

        <p class="period">저축 기간</p>
        <select class="form-select" v-model="period">
          <option selected>기간 선택</option>
          <option> 6개월 </option>
          <option> 12개월 </option>
          <option> 24개월 </option>
          <option> 36개월 </option>
        </select>

        <p class="month">한달 저축 금액</p>
        <select class="form-select" v-model="cost">
          <option selected>금액 선택</option>
          <option>10만원 이하</option>
          <option>30만원 이하</option>
          <option>50만원 이하</option>
          <option>100만원 이하</option>
          <option>200만원 이하</option>
          <option>500만원 이하</option>
          <option>500만원 초과</option>
        </select>

        <button class="btn btn-primary search_btn" @click="getData(bank, period.slice(0, -2))">추천받기</button>
      </div>
    </div>
  </div>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { ref, onMounted } from 'vue'
  import { useFinanceStore } from '@/stores/finance.js'
  
  const store = useFinanceStore()
  const bank = ref('은행 선택')
  const period = ref('기간 선택')
  const cost = ref('금액 선택')
  const depositProductList = ref('')
  const depositOptionList = ref('')
  const savingProductList = ref('')
  const savingOptionList = ref('')

  const prdtListD = ref([])
  const prdtListS = ref([])
  const candidate = ref([])
  const nameList = ref([])
  const recommend = ref([])
  const recommendIntr = ref(0)

  // 금융 상품 정보를 가져오기 위한 함수


  // 3. 2번 중에 intr_rate2 값이 제일 큰 녀석 추천

  const getData = function(bankname, month) {
    nameList.value = []
    recommend.value = []
    candidate.value = []
    recommendIntr.value = 0

    // 1. 은행 정보(bankname) 이용해서 그 은행에 해당하는 상품 정보 받아놓기
    prdtListD.value = depositProductList.value.filter((product) => {
      return product.kor_co_nm === bankname
    })
    prdtListS.value = savingProductList.value.filter((product) => {
      return product.kor_co_nm === bankname
    })

    // 2. 받아 놓은 상품 정보를 이용해서 그 상품의 옵션이 user가 원하는 month와 일치하는 상품을 candidate에 담는다.
    for (const info of prdtListD.value) {
      for (const option of depositOptionList.value) {
        if (info.fin_prdt_cd === option.fin_prdt_cd && option.save_trm == month) {
          candidate.value.push(option)
          nameList.value.push(info.fin_prdt_nm)
        } 
      }    
    }

    for (const info of prdtListS.value) {
      for (const option of savingOptionList.value) {
        if (info.fin_prdt_cd === option.fin_prdt_cd && option.save_trm == month) {
          candidate.value.push(option)
          nameList.value.push(info.fin_prdt_nm)
        } 
      }    
    }

    // 3. candidate에서 최대 우대금리 가진 제품을 추출한다.
    for (const [index, info] of candidate.value.entries()) {
      if (info.intr_rate2 > recommendIntr.value) {
        recommendIntr.value = info.intr_rate2
        recommend.value = nameList.value[index]
      }
    }
  }

  // deposit prdt 와 options를 가져온다.
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/findata/showdepositproducts/`,
    })
      .then((res) =>{
        depositProductList.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  })

  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/findata/showdepositoptions/`,
    })
      .then((res) =>{
        depositOptionList.value = res.data
        })
      .catch((err) => {
        console.log(err)
      })
  })

   // saving prdt 와 options를 가져온다.
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/findata/showsavingproducts/`,
    })
      .then((res) =>{
        savingProductList.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  })
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/findata/showsavingoptions/`,
    })
      .then((res) =>{
        savingOptionList.value = res.data
        })
      .catch((err) => {
        console.log(err)
      })
  })
</script>

<style scoped>
.rec_box {
  margin: 20px 0;
  display: flex;
  /* flex-direction: row; */
  justify-content: center;
}

.recc_box {
  width: 1200px;
}
.title {
  margin-bottom: 20px; 
  font-size: 25px;
  font-weight: bold;
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

/* 추천 목록 on */
.rec_box1 {
  display: flex;
  justify-content: center;
  /* width: 1200px; */
}

.bank_name {
  margin: 5px;
  padding-top:10px;
}

.period {
  margin: 5px;
  padding-top:10px;
}
.month {
  margin: 5px;
  padding-top:10px;
}
.cal_s {
  margin: 0;
}
.cal1 {
  border-radius: 10px;
  background-color: #f7f7f7;
  justify-content: center;
  padding: 30px;
  margin: 10px;
  width: 400px;
  height: 100%;
}
.cal1_2 {
  /* border: 1px solid #f2f2f2; */
  /* border-radius: 10px; */
  /* background-color: #f7f7f7; */
  justify-content: center;
  /* padding: 30px; */
  margin: 10px;
  width: 550px;
}

.cal_e {
  border: 1px solid #e0e0e0;
  padding: 30px;
  border-radius: 10px;
  margin-bottom: 5px;
}

/* 추천 목록 off */
.rec_box2 {
  display: flex;
  justify-content:center;
}

.cal2 {
  justify-content: center;
  padding: 30px;
  margin: 10px 70px;
  background-color: #f7f7f7;
  border-radius: 10px;
  width: 500px;
}
.btn {
    margin-top: 10px;
    padding: 10px;
  }

.search_btn {
  margin-top: 20px;
  width: 100%;
}

.s_title {
  font-size: 20px;
}
</style>