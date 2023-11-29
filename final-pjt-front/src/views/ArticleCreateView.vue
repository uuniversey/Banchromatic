<template>
  <div class="create_box">
  <div class="c_box">
    <form @submit.prevent="createArticle" class="create_form">
      <div class="form_title">게시글 작성</div>
      <div>
        <label for="title">제목</label>
        <input type="text" v-model.trim="title" id="title" class="form-control input_u">
      </div>
      <div>
        <label for="content">내용</label>
        <textarea v-model.trim="content" id="content" class="form-control input_u"></textarea>
      </div>
      <input type="submit" class="btn btn-secondary">
    </form>
</div>
</div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useFinanceStore } from '@/stores/finance'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useFinanceStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'articles' })
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style scoped>
.create_box {
  display: flex;
  justify-content: center;
}

.c_box {
  width: 900px;
  justify-content: center;
  background-color: #f7f7f7;
  padding: 40px 50px;
  border-radius: 10px;
  padding: 50px;
  margin: 50px 0;
}

.create_form {
  padding: 0 50px;
}

.form_title {
  font-weight: bold;
  font-size: 20px;
  margin-bottom: 30px;
}

label {
  margin-bottom: 10px;
  font-size: 15px;
}

.input_u {
  margin-bottom: 20px;
}

.btn-secondary {
  float: right;
  width: 80px;
}
</style>
