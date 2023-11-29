<template>
  <div class="cal_box">
    <div class="cal">
      <div class="title1">💰 환율 계산기</div>

      <!-- 환율 계산하는 곳 -->
      <div class="d-flex flex-row">
        <select class="form-select cal_s" aria-label="Default select example"
        v-model="before">
        <option selected>통화 선택</option>
        <option v-for="curnum in curNumList">{{ curnum }}</option>
      </select>

      <h1>&nbsp;→&nbsp;</h1>

      <select class="form-select" aria-label="Default select example"
        v-model="after"
      >
        <option selected>통화 선택</option>
        <option v-for="curnum in curNumList">{{ curnum }}</option>
      </select>

    </div>

    <div class="align-items-center input_form">
      <form class="m-3 input_m" @submit.prevent="exchangeCalc">
        <label for="amount" class="input_desc">금액</label>
        <input type="number" id="amount" v-model="amount" class="form-control-lg">
      </form>

      <form @submit.prevent="exchangeCalc">
        <input type="submit" class="btn btn-primary search_btn" value="환전">
      </form>

      <p v-if="after==='통화 선택'" class="mx-5 my-3 result_m">
        환전 금액 
        <div>{{ result }}</div>
      </p>
      <p v-else="" class="mx-5 my-3 result_m">
        환전 금액 
        <div>{{ result }} {{ after }} </div>
      </p>

    </div>
    </div>
    </div>
    <div class="info">
    <div class="info_title">
      <div class="title2 align-items-center">환율 정보</div>
  
      <!-- 리스트 띄우는 곳 -->
      <form @change.prevent="showSearchList">
        <select class="ex_all form-select" v-model="search">
          <option>전체보기</option>
          <option v-for="curnum in curNumList">{{ curnum }}</option>
        </select>
      </form>
    </div>

    <!-- 검색 알고리즘 -->
    <div>
      <div v-if="search === '전체보기'" class="e_list">
        <div v-for="exchangerate in exchangeRates">
          <div class="box">
          <p>
            <strong class="ca">통화명</strong>
            {{ exchangerate.cur_nm }}
          </p>
          <p>
            <strong class="ca">통화 코드</strong>
            {{ exchangerate.cur_unit }}
          </p>
          <p>
            <strong class="ca">송금 받을 때</strong>
            {{ exchangerate.ttb }}
          </p>
          <p>
            <strong class="ca">송금 보낼때</strong>
            {{ exchangerate.tts }}
          </p>
          <p>
            <strong class="ca">장부가격</strong>
            {{ exchangerate.bkpr }}
          </p>
          <!-- <p>통화 코드 {{ exchangerate.cur_unit }}</p>
          <p>송금 받을때 {{ exchangerate.ttb }}</p>
          <p>송금 보낼때 {{ exchangerate.tts }}</p>
          <p>장부가격 {{ exchangerate.bkpr }}</p> -->
        </div>
        </div>
      </div>

      <div v-else class="e_list">
        <div v-for="list in searchList">
          <div class="box1">
            <!-- <p>통화명 : {{ list.cur_nm }}</p>
            <p>통화 코드 : {{ list.cur_unit }}</p>
            <p>송금 받을때 : {{ list.ttb }}</p>
            <p>송금 보낼때 : {{ list.tts }}</p>
            <p>장부가격 : {{ list.bkpr }}</p> -->
            <p>
              <strong class="ca">통화명</strong>
              {{ list.cur_nm }}
            </p>
            <p>
              <strong class="ca">통화 코드</strong>
              {{ list.cur_unit }}
            </p>
            <p>
              <strong class="ca">송금 받을 때</strong>
              {{ list.ttb }}
            </p>
            <p>
              <strong class="ca">송금 보낼때</strong>
              {{ list.tts }}
            </p>
            <p>
              <strong class="ca">장부가격</strong>
              {{ list.bkpr }}
            </p>
          </div>
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
  const exchangeRates = ref('')
  const curNumList = ref([])
  const amount = ref(0)
  const result = ref(0)
  const search = ref('전체보기')
  const searchList = ref([])
  const before = ref('통화 선택')
  const after = ref('통화 선택')

  // 환전 하는 함수
  const exchangeCalc = function () {
    axios({
      method: 'get',
      url: `${store.API_URL}/findata/exchange_calc/${before.value}/${after.value}/`,
    })
      .then((res) =>{
       result.value = res.data
       result.value *= amount.value
       result.value = result.value.toLocaleString()
      })
      .catch((err) => {
        console.log(err)
      })
  }


  // 환율 정보 리스트 만드는 함수
  const showSearchList = function () { 
    const list = exchangeRates.value.filter(element => {
      return element.cur_nm === search.value
    })
    searchList.value = list
  }
  
  // 전체 환율 정보 받아오기
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/findata/showexchangerates/`,
    })
      .then((res) =>{
        exchangeRates.value = res.data

        exchangeRates.value.forEach(element => {
          curNumList.value.push(element.cur_nm)
        })
      })
      .catch((err) => {
        console.log(err)
      })
  })

</script>

<style scoped>
.cal_box {
  display: flex;
  margin: 30px 0;
  justify-content: center;
}

.title1 {
  margin-bottom: 20px; 
  font-size: 20px;
  font-weight: bold;
}

.cal {
  /* border: 1px solid #f2f2f2; */
  background-color: #f8f8f8;
  justify-content: center;
  padding: 30px;
  margin: 10px 70px;
  width: 900px;
}
.cal_s {
  margin: 0 auto;
}

/* 금액 입력창 */
.input_form {
  display: flex;
}

/* .input_m {
  display: flex;
  flex-direction: column;
} */

.input_desc {
  font-size: 17px;
  margin-right: 10px;
}

.btn {
  padding: 10px 20px;
}

.result_m {
  font-weight: bold;
}

/* exchangerate list */
.info {
  border: 1px solid #f7f7f7;
  padding: 40px 0;
  justify-content: center;
  margin: 0 auto;
  width: 900px;
  margin-bottom: 60px;
  /* margin: 0 0 30px 0; */
}
.title2 {
  padding: 0 0 20px 10px;
  font-size: 20px;
  font-weight: bold;
  margin-right: 30px;
}
.info_title {
  display: flex;
  justify-content: center;
}

.ex_all {
  width: 300px;
}

.e_list {
  padding: 25px;
  /* border: 1px solid #f2f2f2; */
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.e_list .box {
  border: 1px solid #e0e0e0;
  padding: 20px;
  margin: 13px;
  width: 255px;
  height: 300px;
  border-radius: 3%;
}

/* .result {
  display: flex;
  flex-direction: column;
  height: 30px;
} */

.ca {
  font-size: 15px;
}

.box1{
  border: 1px solid #e0e0e0;
  padding: 55px 20px 20px 50px;
  margin: 13px;
  width: 600px;
  height: 300px;
  border-radius: 3%;
  display: flex;
  flex-direction: column;
}
</style>