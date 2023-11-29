<template>
  <div class="board_box">
    <div class="title">✏ 게시판</div>
    <div class="content">
      <RouterLink :to="{name: 'notice'}">공지사항</RouterLink>  |
      <RouterLink :to="{name: 'faq'}">자주 묻는 질문</RouterLink> |
      <!-- <RouterLink :to="{name: 'questions'}">Q&A</RouterLink> | -->
      <RouterLink :to="{name: 'articles'}">금융 상품 후기</RouterLink>
    </div>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
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
  margin-top: 30px;
}
.content {
  text-align: center;
  
}
.content a {
  text-decoration: none;
  color: black;
  padding: 20px;
}
</style>