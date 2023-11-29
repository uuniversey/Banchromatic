<template>
  <div class="board_box">
    <div class="title">✏ Q&A</div>
    <div class="content">
      <RouterLink :to="{name: 'notice'}">공지사항</RouterLink>  |
      <RouterLink :to="{name: 'faq'}">자주 묻는 질문</RouterLink> |
      <RouterLink :to="{name: 'questions'}">Q&A</RouterLink> |
      <RouterLink :to="{name: 'articles'}">금융 상품 후기</RouterLink>
    </div>
  </div>
  <div class="create_btn">
    <RouterLink :to="{ name : 'createquestion'}">
      <button type="button" class="btn btn-outline-secondary">게시글 작성</button>
    </RouterLink>
  </div>
    <QuestionList />
</template>

<script setup>
import { onMounted } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import { RouterLink } from 'vue-router'
import QuestionList from '@/components/QuestionList.vue'

const store = useFinanceStore()

onMounted(() => {
  store.getQuestions()
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
  
}
.content a {
  text-decoration: none;
  color: black;
  padding: 20px;
}

.create_btn {
  margin: 0 70px;
}
.questionlist {
  margin: 20px 70px;
}
</style>