<template>
  <div class="questionlist">
    <QuestionListItem 
      v-for="question in store.questions"
      :key="question.id"
      :question="question"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import QuestionListItem from '@/components/QuestionListItem.vue'

const store = useFinanceStore()
</script>

<style scoped>
.questionlist {
  color: black;
  text-decoration: none;
}
</style>