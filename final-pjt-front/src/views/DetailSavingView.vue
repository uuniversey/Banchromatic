<template>
  <div class="p_detail_box">
    <div class="p_detail">
      <div class="detail1">
    <nav class="my-3">
      <RouterLink :to="{ name: 'deposit' }">정기예금</RouterLink> |
      <RouterLink :to="{ name: 'saving' }">정기적금</RouterLink>
    </nav>

    <div class="detail_page">
    <div class="d-flex justify-content-between">
      <div class="title">적금 상품 상세 페이지</div>
      <button class="btn-sm btn btn-secondary before_btn" @click="goBefore">이전 페이지로</button>
    </div>

    <div class="mt-5 detail_info">
      <table>
        <tr>
          <td class="info_1">은행명</td>
          <td>{{ info.kor_co_nm }}</td>
        </tr>
        <tr>
          <td>상품명</td>
          <td>{{ info.fin_prdt_nm }}</td>
        </tr>
        <tr>
          <td>금융 상품 설명</td>
          <td>{{ info.etc_note }}</td>
        </tr>
        <tr>
          <td>가입 제한</td>
          <td>{{ info.join_deny }}</td>
        </tr>
        <tr>
          <td>가입 방법</td>
          <td>{{ info.join_way }}</td>
        </tr>
        <tr>
          <td>가입 대상</td>
          <td>{{ info.join_member }}</td>
        </tr>
        <tr>
          <td>우대조건</td>
          <td>{{ info.spcl_cnd }}</td>
        </tr>
      </table>
      <!-- <p>은행명 : {{ info.kor_co_nm }}</p>
      <p>상품명 : {{ info.fin_prdt_nm }}</p>
      <p>금융 상품 설명 : {{ info.etc_note }}</p>
      <p>가입 제한 : {{ info.join_deny }}</p>
      <p>가입 방법 : {{ info.join_way }}</p>
      <p>가입 대상 : {{ info.join_member }}</p>
      <p>우대조건 : {{ info.spcl_cnd }}</p> -->

      <div v-if="store.isLogin" class="save_btn">
        <button class="btn btn-outline-secondary save_b" @click="joinProduct()">가입하기</button>
        <button class="btn btn-outline-secondary save_b" @click="deleteProduct()">가입해지</button>
      </div>
      </div>
    </div>
      </div>
      </div>
    </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useRoute, useRouter} from 'vue-router'
import { ref } from 'vue'
import { useFinanceStore } from '@/stores/finance.js'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useFinanceStore()
const info = ref('')

// detail 정보를 info로 가져오기 위한 url
axios({
  method: 'get',
  url: `${store.API_URL}/findata/detail_s/${route.params.conm}/`,
})
  .then((res) =>{
    info.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })

// 상품 가입하는 함수
const joinProduct = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/user/join_saving/${store.userInfo.username}/`,
    data: {
      prdtcd: route.params.conm
    }
  })
    .then((res) =>{
      window.alert('가입 완료 되었습니다.')
    })
    .catch((err) => {
      console.log(err)
    })
}

// 상품 해지하는 함수
const deleteProduct = function() {
  axios({
    method: 'delete',
    url: `${store.API_URL}/user/delete_saving/${store.userInfo.username}/`,
    data: {
      prdtcd: route.params.conm
    }
  })
    .then((res) =>{
      window.alert('가입 해지 되었습니다.')
    })
    .catch((err) => {
      console.log(err)
    })
}

// 이전 페이지로 이동하는 함수
const goBefore = function () {
  router.go(-1)
}
</script>

<style scoped>
.p_detail_box {
  display: flex;
  justify-content: center;
}

.p_detail {
  width: 1200px;
  display: flex;
  justify-content: center;
}

.detail1 {
  justify-content: center;
}
  
a {
  text-decoration: none;
}

a:visited {
  color:black
}

.btn {
  margin: 10px 10px 0 0;
  padding: 10px;
}

.title {
  padding: 0 20px 0 20px;
  font-weight: bold;
  font-size: 20px;
  margin-top: 10px;
}

.detail_info {
  /* margin: 0 20px 0 20px; */
  padding: 0 20px;
  border: 1px solid #f7f7f7;
  border-radius: 10px;
  width: 800px;
}

.detail_page {
  background-color: #f7f7f7;
  padding: 50px;
  width: 1000px;
  justify-content: center;
}

.before_btn {
  margin: 0;
}

.info_1 {
  width: 200px;
}

table {
  height: 300px;
  margin-bottom: 20px;
}

td:nth-child(1) {
  font-weight: bold;
}

.save_b {
  padding: 10px 20px;
}
</style>