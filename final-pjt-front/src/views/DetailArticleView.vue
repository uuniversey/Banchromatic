<template>
  <div class="detail_box">
    <div class="article_detail">
    <div v-if="article">
      <div class="article_title">
        <p class="title">{{ article.title }}</p>
        <div class="article_info">
        <p class="user">작성자 : {{ article.user.username }}</p>
        <p>작성일 : {{ article.created_at.slice(0, 10) }}</p>
      </div>
      </div>
      <hr>
      <!-- <p>작성일 : {{ article.created_at.slice(0, 10) }}</p> -->
      <p class="article_content">{{ article.content }}</p>
      <div class="article_btn">
      <RouterLink :to="{ name: 'updatearticle', params: {id: article.id}}">
        <button type="button" class="btn btn-secondary m-1">게시글 수정</button>
      </RouterLink>
        <button type="button" class="btn btn-secondary" @click="articleDelete">게시글 삭제</button>
      </div>
      </div>
    <CreateComment 
      :article-id="articleId"/>
    <CommentList />
    <RouterLink style="text-decoration: none;" :to="{name: 'articles'}" class="list_btn">목록으로</RouterLink>
  </div>
</div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import { useRoute, useRouter, RouterLink } from 'vue-router'
import CommentList from '../components/CommentList.vue'
import CreateComment from '@/components/CreateComment.vue'

const store = useFinanceStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const articleId = ref(null)
const token = ref(null)

onMounted(() => {
  for (article in store.articles.value) {
    console.log(article)
  }
})

onMounted(() => {
  store.getComments()
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
      articleId.value = article.value.id
    })
    .catch((err) => {
      console.log(err)
    })
})

const articleDelete = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      // console.log(res.data)
      router.push({ name: 'articles' })
      store.getArticle()
      c
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>
.detail_box {
  display: flex;
  justify-content: center;
}

.article_detail {
  width: 900px;
  justify-content: center;
  background-color: #f7f7f7;
  padding: 40px 50px;
  border-radius: 10px;
  margin: 50px 0;
}

.article_btn {
  padding: 10px 50px;
  float: right;
}

.article_title {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 30px;
  margin: 0 50px;
}

.article_info {
  display: flex;
  font-size: 14px;
}

.title {
  font-weight: bold;
  font-size: 20px;
}

.user {
  margin-right: 20px;
}
.article_content {
  height: 200px;
  padding: 20px 0 0 0;
  /* background-color: white; */
  margin: 0 50px;
}

/* .tolist {
  display: flex;
  justify-content: center;
  width: 1200px;
} */

.list_btn {
  color: black;
}
</style>
  