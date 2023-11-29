<template>
  <div class="signup_page">
    <div class="signup_box">
      <div class="title">☑ 회원가입</div>
      <hr>
      <form @submit.prevent="signUp" class="d-flex flex-column sign_up">
        <label for="id"></label>
        <input type="text" id="id" v-model.trim="username" class="form-control" placeholder="아이디를 입력하세요">
        <label for="pw1"></label>
        <input type="password" id="pw1" v-model.trim="password1" class="form-control" placeholder="비밀번호">
        <label for="pw2"></label>
        <input type="password" id="pw2" v-model.trim="password2" class="form-control" placeholder="비밀번호 확인">
        <label for="name"></label>
        <input type="text" id="name" v-model.trim="nickname" class="form-control" placeholder="이름">
        <label for="age"></label>
        <input type="number" id="age" v-model.trim="age" class="form-control" placeholder="나이">
        <label for="money"></label>
        <input type="number" id="money" v-model.trim="money" class="form-control" placeholder="자산">
        <label for="salary"></label>
        <input type="number" id="salary" v-model.trim="salary" class="form-control" placeholder="연봉">
        <input type="submit" value="회원가입" class="btn btn-primary">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)


const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    age: age.value,
    money: money.value,
    salary: salary.value
  }

  store.signUp(payload)
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
