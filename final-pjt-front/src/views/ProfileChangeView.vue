<template>
  <div>
    <div class="signup_page">
      <div class="signup_box">
        <div class="title">☑ 프로필 변경</div>
        <form @submit.prevent="changeProfile" class="d-flex flex-column sign_up">
          <label for="id">id</label>
          <input type="text" id="id" v-model.trim="username" class="form-control" :placeholder="`${profile.username}`" disabled>
          <label for="name">이름</label>
          <input type="text" id="name" v-model.trim="nickname" class="form-control" :placeholder="`${profile.nickname}`">
          <label for="age">나이</label>
          <input type="number" id="age" v-model.trim="age" class="form-control" :placeholder="`${profile.age}`">
          <label for="money">자산</label>
          <input type="number" id="money" v-model.trim="money" class="form-control" :placeholder="`${profile.money}`">
          <label for="salary">연봉</label>
          <input type="number" id="salary" v-model.trim="salary" class="form-control" :placeholder="`${profile.salary}`">
          <input type="submit" value="프로필 변경" class="btn btn-primary">
        </form>

      </div>
    </div>
  </div>



</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useFinanceStore } from '@/stores/finance.js'
import axios from 'axios'

const store = useFinanceStore()
const route = useRoute()
const router = useRouter()
const profile = ref('')
const money = ref('')
const salary = ref('')
const username = ref(null)
const nickname = ref(null)
const age = ref(null)

// 유저 정보를 가져오는 axios
onMounted(() =>{
  axios({
    method: 'get',
    url: `${store.API_URL}/user/profile/${route.params.conm}/`,
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

// 프로필 변경하는 함수
const changeProfile = function () {
  
   axios({
    method: 'put',
    url: `${store.API_URL}/user/profilechange/${route.params.conm}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      username: route.params.conm,
      nickname: nickname.value,
      age: age.value,
      money: money.value,
      salary: salary.value
    },
  })
    .then((res) => {
      console.log(res)
      router.push({ name: 'profile', params: { id: route.params.conm } })
    })
    .catch((err) => {
      console.log(err)
    })

}



</script>

<style scoped>
  .signup_page {
    display: flex;
    justify-content: center;
    margin-top: 20px;
  }
  .signup_box {
    margin-top: 20px;
    width: 500px;
    background-color: #f7f7f7;
    border-radius: 10px;
    padding: 30px;
  }

  .form-control {
    padding: 10px;
  }
  .title {
    font-weight: bold;
    font-size: 25px;
    margin-bottom: 20px;
    text-align: center;
  }

  .sign_up {
    margin: 40px 20px 20px 20px;
  }

  label {
    font-weight: bold;
    padding: 0 0 5px 10px;
  }

  input {
    margin-bottom: 10px;
  }

  .btn {
    margin-top: 10px;
    padding: 10px;
  }
</style>