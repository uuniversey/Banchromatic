<template>
  <div class="question_box">
    <div v-if="question">
      <div class="question_title">
        <p>{{ question.title }}</p>
        <p>작성자 : {{ question.user }}</p>
      </div>
      <hr>
      <p>작성일 : {{ question.created_at }}</p>
      <p class="question_content">{{ question.content }}</p>
      <p>[save]</p>
      <p>목록으로</p>
    </div>
    <!-- <RouterLink :to="{ name: 'updatequestion', params: {id: question.id}}"> -->
        <button type="button" class="btn btn-outline-secondary">게시글 수정</button>
      <!-- </RouterLink> -->
      <p @click="questionDelete">
        <button type="button" class="btn btn-outline-secondary">게시글 삭제</button>
      </p>
      <hr>
  </div>
  <!-- <CreateAnswer 
      :question-id="questionId"/>
  <AnswerList /> -->
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import { useRoute, useRouter } from 'vue-router'
import AnswerList from '../components/AnswerList.vue'
import CreateAnswer from '@/components/CreateAnswer.vue'

const store = useFinanceStore()
const route = useRoute()
const router = useRouter()
const question = ref(null)
const questionId = ref(null)

onMounted(() => {
  store.getComments()
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/questions/${route.params.id}/`
  })
    .then((res) => {
      question.value = res.data
      questionId.value = question.value.id
    })
    .catch((err) => {
      console.log(err)
    })
})

const questionDelete = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/questions/${route.params.id}/`,
  })
    .then((res) => {
      // console.log(res.data)
      router.push({ name: 'answers' })
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>
.question_box {
  margin: 50px;
}
.question_content {
  height: 100px;
}
</style>
  