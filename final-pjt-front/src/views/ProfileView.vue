<template>
  <div class="p_box">
    <div class="profile">
    <div class="d-flex justify-content-between mt-3">
      <div class="title"> 👤 프로필</div>
      <button 
        class="btn-sm btn btn-outline-primary"
        @click="goChange(profile.username)"
      >
      프로필 변경하기</button>
    </div>
    <hr>
    <div class="user_info">
    <div class="info">
      <img src="@/img/profile.png" alt="" class="p_img">
      <p>id : {{ profile.username }}</p>
      <p>이름 : {{ profile.nickname }}</p>
      <p>나이 : {{ profile.age }} 세</p>
      <p>자산 : {{ profile.money }} ₩</p>
      <p>연봉 : {{ profile.salary }} ₩</p>
    </div>
    <div class="prdt_save">

    <p>예금 가입 상품</p>
    <div class= "d-flex align-items-center p_save" v-for="deposit, index in depositProductInfo">
       <span>{{ index + 1 }}. {{ deposit.kor_co_nm }} {{ deposit.fin_prdt_nm }}</span>
       <button class="btn-sm btn btn-outline-secondary" @click="showDetail_deposit(deposit.fin_prdt_cd)">상세정보</button>
    </div>
    <hr>

    <p>적금 가입 상품</p>
    <div class= "d-flex align-items-center p_save" v-for="saving, index in savingProductInfo">
      <span>{{ index + 1 }}. {{ saving.kor_co_nm }} {{ saving.fin_prdt_nm }}</span>
      <button class="btn-sm btn btn-outline-secondary" @click="showDetail_saving(saving.fin_prdt_cd)">상세정보</button>
    </div>
  </div>
</div>
</div>
  </div>
</template>

<script setup>
  import { RouterLink, RouterView, useRouter, useRoute } from 'vue-router'
  import { ref, onMounted } from 'vue'
  import { useFinanceStore } from '@/stores/finance.js'
  import axios from 'axios'

  const profile = ref('')
  const route = useRoute()
  const router = useRouter()
  const store = useFinanceStore()
  const money = ref('')
  const salary = ref('')
  const depositProductInfo = ref('')
  const savingProductInfo = ref('')

  // 유저 정보를 가져오는 axios
  onMounted(() =>{
    axios({
      method: 'get',
      url: `${store.API_URL}/user/profile/${route.params.id}/`,
    })
      .then((res) => {
        profile.value = res.data
        profile.value.money = profile.value.money.toLocaleString()
        profile.value.salary = profile.value.salary.toLocaleString()
      })
      .catch((err) => {
        console.log(err)
      })
    })

  // 가입 예금 상품을 가져오는 axios
  onMounted(() =>{
    axios({
      method: 'get',
      url: `${store.API_URL}/user/registered_deposit/${route.params.id}/`,
    })
      .then((res) => {
        depositProductInfo.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    })

  // 가입 적금 상품을 가져오는 axios
  onMounted(() =>{
    axios({
      method: 'get',
      url: `${store.API_URL}/user/registered_saving/${route.params.id}/`,
    })
      .then((res) => {
        savingProductInfo.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    })
  
  // 프로필에서 상세정보로 각 상품 보는 함수
  const showDetail_deposit = function (element) {
    router.push({ name: 'detaildeposit', params: { conm: element } })
  }

  const showDetail_saving = function (element) {
    router.push({ name: 'detailsaving', params: { conm: element } })
  }

  // 프로필 변경하는 페이지로 이동하는 함수
  const goChange = function(element) {
    router.push({ name: 'profilechange', params: { conm: element } })
  } 

</script>

<style scoped>
.p_box {
  display: flex;
  justify-content: center;
}

.profile {
  width: 1000px;
  padding: 30px 50px;
  background-color: #f7f7f7;
  margin: 20px;
}

.title {
  font-weight: bold;
  font-size: 24px;
}

.user_info {
  display: flex;
  margin-top: 40px;
}
.info {
  /* border: 1px solid #c0c0c0; */
  background-color: white;
  border-radius: 10px;
  width: 380px;
  height: 540px;
  padding: 40px 64px;
  justify-content: center;
  /* flex-direction: column; */
  font-size: 17px;
  margin-right: 50px;
}

.p_img {
  width: 250px;
  margin-bottom: 20px;
}

.prdt_save {
  width: 500px;
}

.prdt_save p {
  font-weight: bold;
  font-size: 20px;
}

.p_save{
  justify-content: space-between;
}

.p_save button {
  margin-bottom: 5px;
}

.btn {
  padding: 10px;
  margin-left: 10px;
}
</style>