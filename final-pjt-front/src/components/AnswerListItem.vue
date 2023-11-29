<template>
  <div class="comment_item">
  <RouterLink :to="{name : 'DetailArticle', params: {id: comment.id}}">
  <div class="comment">
    <!-- <p>{{ review.id }}</p> -->
    <p>작성자 {{ comment.user }}</p>
    <p>{{ comment.content }}</p>
  </div>
  </RouterLink>
  <div @click="commentdelete">[delete]</div>
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
}

.comment {
  text-decoration: none;
  display: flex;
  flex-direction: column;
  color: black;
}

</style>