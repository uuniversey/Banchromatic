<template>
  <div class="main">
    <div class="header">
      <div class="header1">
      <nav class="navbar">
        <RouterLink :to="{ name: 'home' }">
          <img src="@/img/logo.png" alt="">
        </RouterLink>
        <RouterLink :to="{ name: 'exchangerate' }">환율 계산</RouterLink>
        <RouterLink :to="{ name: 'deposit' }">예적금 비교</RouterLink>
        <RouterLink :to="{ name: 'map' }">주변 은행 찾기</RouterLink>
        <RouterLink :to="{ name: 'recommend' }">금융 상품 추천</RouterLink> 
        <RouterLink :to="{ name: 'notice' }">게시판</RouterLink>
      </nav>

      <div class="sign">
      <p v-if="store.isLogin" class="loginout">
          <!-- <RouterLink :to="{ name: 'home' }">메인페이지로</RouterLink> | -->
          <form @submit.prevent="store.logOut">
            <input type="submit" class="logout" value="로그아웃">
          </form> | &nbsp;
          <RouterLink :to="{name : 'profile', params : { id: store.userInfo.username }}">내 프로필</RouterLink>
        </p>
        <p v-else class="loginout1">
          <p><RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink></p>
          <p><RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink></p>
        </p>
        </div>
    </div>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()

</script>

<style scoped>

/* header */
.header {
  padding-top: 20px;
  border-bottom: 1px solid #e0e0e0;
  display: flex;
  justify-content: center;
}

.header1{
  width: 1200px;
  display: flex;
  justify-content: space-between;
  /* background-color: #f7f7f7; */
}
.sign {
  display: flex;
  justify-content: space-around;
  align-items: bottom;
  font-size: 20px;
  width: 200px;
  padding-top: 30px;
  margin-top: 18px;
}
.sign a {
  text-decoration: none;
  color: black;
  font-size: 15px;
}

.loginout {
  display: flex;
  justify-content: space-around;
  display: flex;
  padding: 0;
  align-items: center;
  font-size: 13px;
  margin-right: 30px;
  margin-bottom: 45px;
  width: 150px;
}

.loginout1 {
  display: flex;
  justify-content: space-around;
  display: flex;
  padding: 0;
  align-items: center;
  font-size: 13px;
  margin-right: 30px;
  margin-bottom: 30px;
  width: 150px;
}

.logout {
  color: black;
  border: none;
  background-color: white;
  height: 20px;
  font-size: 15px;
  margin-bottom: 5px;
}

nav {
  display: flex;
  padding: 10px;
  /* margin-top: 20px; */
  color: black;
}

nav a {
  text-decoration: none;
  color: black;
  margin: 0 30px;
}

/* nav a:visited {
  color:white;
} */

img {
  width: 140px;
}


</style>