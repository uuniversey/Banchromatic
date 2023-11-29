<template>
  <div class="answers">
      <p>댓글</p>
        <form @submit.prevent="createAnswer">
          <div>
          <label for="content"></label>
          <textarea v-model.trim="content" id="content"></textarea>
          </div>
          <input type="submit">
      </form>
      <hr>
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
  answerId: Number
})

console.log(props)

const createAnswer = function () {
axios({
  method: 'post',
  url: `${store.API_URL}/api/v1/questions/${props.answerId}/comments/`,
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
    router.push({ name: 'DetailQuestion'})
  })
  .catch((err) => {
    console.log(err)
  })
}

</script>

<style scoped>

</style>