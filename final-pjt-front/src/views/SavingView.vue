<template>
  <div class="inter_box">
    <div class="inter_b">
    <div class="inter_content">
    <div class="inter_nav">
      <div class="title">금리 비교</div>
      <RouterLink :to="{ name: 'deposit' }">정기예금</RouterLink> |
      <RouterLink :to="{ name: 'saving' }">정기적금</RouterLink>
    </div>

    <div class="search_f">
      <form @change.prevent="showSearchList" class="search_form">
        <select class="form-select select_de" v-model="search">
          <option>전체보기</option>
          <option v-for="bank in bankList">{{ bank }}</option>
        </select>
      </form>
    </div>

  <!-- 검색 알고리즘 및 예금,적금 리스트 출력-->
  <div class="p_list">
  <table class="product_list">
    <thead class="">
      <tr class="line">
        <th>금융회사명</th>
        <th>상품명</th>
        <th>6개월</th>
        <th>12개월</th>
        <th>24개월</th>
        <th>36개월</th>
      </tr>
    </thead>

    <tbody v-if="search === '전체보기'">
      <tr v-for="product in savingProductList" class="line">
        <td>{{ product.kor_co_nm }}</td>
        <td>{{ product.fin_prdt_nm }}</td>
        <td>{{ getOption(product.fin_prdt_cd, 6) }}</td>
        <td>{{ getOption(product.fin_prdt_cd, 12) }}</td>
        <td>{{ getOption(product.fin_prdt_cd, 24) }}</td>
        <td>{{ getOption(product.fin_prdt_cd, 36) }}</td>
        <td>
          <button class="info_btn" @click="showDetail(product.fin_prdt_cd)">상세정보</button>
        </td>
      </tr>
    </tbody>
    <tbody v-else>
      <tr v-for="list in searchList" class="line">
        <td>{{ list.kor_co_nm }}</td>
        <td>{{ list.fin_prdt_nm }}</td>
        <td>{{ getOption(list.fin_prdt_cd, 6) }}</td>
        <td>{{ getOption(list.fin_prdt_cd, 12) }}</td>
        <td>{{ getOption(list.fin_prdt_cd, 24) }}</td>
        <td>{{ getOption(list.fin_prdt_cd, 36) }}</td>
        <td>
          <button class="info_btn" @click="showDetail(list.fin_prdt_cd)">상세정보</button>
        </td>
      </tr>
    </tbody>
  </table>
</div>
</div>
</div>
</div>
  <RouterView />
</template>

<script setup>
  import { RouterLink, RouterView, useRouter } from 'vue-router'
  import { ref, onMounted } from 'vue'
  import { useFinanceStore } from '@/stores/finance.js'
  import axios from 'axios'
  
  const store = useFinanceStore()
  const savingProductList = ref('')
  const savingOptionList = ref('')
  const search = ref('전체보기')
  const searchList = ref([])
  const bankList = ref([])
  
  const router = useRouter()
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/findata/showsavingproducts/`,
    })
      .then((res) =>{
        savingProductList.value = res.data
        savingProductList.value.forEach(element => {
          if (!bankList.value.includes(element.kor_co_nm)) {
            bankList.value.push(element.kor_co_nm)
          }
        })
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

  // detail 페이지로 가는 함수
  const showDetail = function (element) {
    router.push({ name: 'detailsaving', params: { conm: element } })
  }

  // select 하기 위한 리스트 만드는 함수
  const showSearchList = function () { 
    const list = savingProductList.value.filter(element => {
      return element.kor_co_nm === search.value
    })
    searchList.value = list
  }

  // 해당 하는 개월의 option 정보를 뽑는 함수
  const getOption = function(standard, num) {
    if (savingOptionList.value) {
      const info = savingOptionList.value.find((option) => {
        return option.fin_prdt_cd === standard && option.save_trm === num
      })
      if (info && info.intr_rate2) {
        return info.intr_rate2
      } else {
        return '-'
      }
    }
  }
  

</script>

<style scoped>
.inter_box {
  display: flex;
  justify-content: center;
}

.inter_content {
  margin: 20px;
}

.inter_b {
  width: 1200px;
  display: flex;
}

.title {
  padding: 0 0 20px 0;
  font-weight: bold;
  font-size: 20px;
}

a {
  text-decoration: none;
}

a:visited {
  color:black
}
.select_de {
  justify-content: center;
  width: 500px;
}
.box {
  border: 1px solid #f2f2f2;
  border-radius: 3%;
}
.line {
  border-bottom: 1px solid silver;
}

button {
  border: 1px 
}

.search_form {
  margin-top: 20px;
  width: 1000px;
}

/* product list */
.product_list {
  margin-top: 20px;
  width: 1100px;
}

.info_btn {
  padding: 7px 10px;
  margin: 5px 0;
  font-size: 15px;
}
</style>