<template>
  <div class="board_box">
    <div class="title">✏ 금융 상품 후기</div>
    <div class="content">
      <RouterLink :to="{ name: 'notice'}">공지사항</RouterLink>  |
      <RouterLink :to="{ name: 'faq'}">자주 묻는 질문</RouterLink> |
      <!-- <RouterLink :to="{ name: 'questions'}">Q&A</RouterLink> | -->
      <RouterLink :to="{ name: 'articles'}">금융 상품 후기</RouterLink>
    </div>
  </div>
  <div class="create_btn">
    <div class="c_btn">
    <RouterLink :to="{ name : 'createarticle'}">
      <button type="button" class="btn btn-outline-secondary">게시글 작성</button>
    </RouterLink>
  </div>
  </div>
  <div class="article">
    <div class="article_list">
    <ArticleList />
  </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useFinanceStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style scoped>
.board_box {
  margin: 20px 0;
}
.title {
  font-weight: bold;
  font-size: 25px;
  margin-bottom: 20px;
  text-align: center;
}
.content {
  text-align: center;
  text-decoration: none;
  /* width: 1200px; */
}
.content a {
  text-decoration: none;
  color: black;
  padding: 20px;
}

.create_btn {
  justify-content: center;
  display: flex;
}

.c_btn {
  width: 1200px;
  justify-content: center;
  display: flex;
  margin: 30px;
  float:right;
}
.article {
  justify-content: center;
  display: flex;
}

.article_list {
  width: 1200px;
  justify-content: center;
}

</style>