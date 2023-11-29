<template>
  <div class="login_page">
    <div class="login_box">
      <div class="title">☑ 로그인</div>
      <hr>
      <form @submit.prevent="logIn" class="d-flex flex-column log_in">
        <label for="id"></label>
        <input type="text" id="id" v-model.trim="username" class="form-control" placeholder="아이디를 입력하세요">
        <label for="pw1"></label>
        <input type="password" id="pw1" v-model.trim="password" class="form-control" placeholder="비밀번호">
        <input type="submit" value="로그인" class="btn btn-primary">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>
.login_page {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
.login_box {
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

.log_in {
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
