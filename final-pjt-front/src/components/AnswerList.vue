<template>
  <div class="commentlist">
    <AnswerListItem 
      v-for="comment in store.comments"
      :key="comment.id"
      :comment="comment"
      />
  </div>
</template>

<script setup>
import { useFinanceStore } from '@/stores/finance'
import AnswerListItem from '@/components/AnswerListItem.vue'


const store = useFinanceStore()
console.log(store.comments)
</script>

<style scoped>
.commentlist {
  color: black;
  text-decoration: none;
}
</style>