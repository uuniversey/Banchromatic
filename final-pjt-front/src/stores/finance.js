import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useFinanceStore = defineStore('finance', () => {
  const router = useRouter()
  const articles = ref([])
  const questions = ref([])
  const comments= ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const userInfo = ref([])
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getQuestions = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/questions/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        questions.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getComments = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/comments/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2, nickname, age, money, salary } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname, age, money, salary
      }
    })
      .then((res) => {
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        userInfo.value = payload
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  return { articles, questions, comments, API_URL, getArticles, getQuestions, getComments, signUp, logIn, token, isLogin, logOut, userInfo}
}, { persist: true })