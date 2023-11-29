<template>
  <div class="commentlist">
    <p><strong>댓글</strong></p>
    
    <CommentListItem 
      v-for="(comment, index) in store.comments"
      :key="comment.id"
      :comment="comment"
      :index="index"
      />
  </div>
</template>

<script setup>
import { useFinanceStore } from '@/stores/finance'
import CommentListItem from '@/components/CommentListItem.vue'


const store = useFinanceStore()
console.log(store.comments)
</script>

<style scoped>
strong {
  padding: 0 50px;
  justify-content: center;
  font-size: 18px;
}
.commentlist {
  color: black;
  text-decoration: none;
}
</style>