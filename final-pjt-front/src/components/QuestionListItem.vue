<template>
  <div class="question_item">
  <RouterLink :to="{name : 'DetailQuestion', params: {id: question.id}}">
  <div class="question">
    <!-- <p>{{ review.id }}</p> -->
    <p>{{ question.title }}</p>
    <p>{{ question.user }}</p>
  </div>
  </RouterLink>
  </div>
  <hr>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  question: Object,
})
</script>

<style scoped>
.question_item {
  padding: 0 50px;
  height: 20px;
}

.question {
  text-decoration: none;
  display: flex;
  justify-content: space-between;
  color: black;
}

</style>