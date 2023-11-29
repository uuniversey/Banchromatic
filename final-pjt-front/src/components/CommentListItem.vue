<template>
  <div class="comment_item">
  <!-- <RouterLink :to="{name : 'DetailArticle', params: {id: comment.id}}"> -->
  <div class="comment_e">
    <div class="comment">
    <!-- <p>{{ review.id }}</p> -->
    <p>작성자 {{ comment.user.username }}</p>
    <p>{{ comment.content }}</p>
    
  </div>
  <!-- </RouterLink> -->
  <button @click="commentdelete" class="btn btn-secondary">삭제</button>
  </div>
</div>
  <hr>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()
const route = useRoute()
const router = useRouter()

const props = defineProps({
  comment: Object,
  index: Number
})

const commentdelete = function() {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/comments/${props.comment.id}/`,
  })
    .then((res) => {
      location.reload()
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>
.comment_item {
  padding: 0 50px;
  height: 60px;
}

.comment {
  text-decoration: none;
  display: flex;
  flex-direction: column;
  color: black;
}

.comment_e {
  display: flex;
  justify-content: space-between;
}

.btn-secondary {
  height: 40px;
  margin-top: 10px;
  font-size: 13px;
}

</style>