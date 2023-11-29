<template>
    <div class="answers">
          <form @submit.prevent="createComment">
            <div class="comment_create">
            <label for="answer"></label>
            <div class="input-group mb-1">
            <textarea v-model.trim="content" id="answer" class="form-control" placeholder="댓글을 입력하세요"></textarea>
            <input type="submit" class="btn btn-primary">
          </div>
          </div>
        </form>
      </div>
      
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import { useRoute, useRouter, RouterLink } from 'vue-router'

const store = useFinanceStore()
const route = useRoute()
const router = useRouter()
const content = ref(null)
const props = defineProps({
    articleId: Number
})

console.log(props)

const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${props.articleId}/comments/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // console.log(res)
      content.value = ''
      location.reload()
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>
.input-group {
  padding: 20px 50px;
  display: flex;
  justify-content: center;
}

.btn {
  padding: 30px;
}
</style>