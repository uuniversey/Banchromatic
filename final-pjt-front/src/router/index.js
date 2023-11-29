import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import InterestRateView from '@/views/InterestRateView.vue'
import MapView from '@/views/MapView.vue'
import RecommendView from '@/views/RecommendView.vue'
import BoardView from '@/views/BoardView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileChangeView from '@/views/ProfileChangeView.vue'
import DepositView from '@/views/DepositView.vue'
import SavingView from '@/views/SavingView.vue'
import NoticeView from '@/views/NoticeView.vue'
import FaqView from '@/views/FaqView.vue'
import QuestionView from '@/views/QuestionView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import DetailDepositView from '@/views/DetailDepositView.vue'
import DetailSavingView from '@/views/DetailSavingView.vue'
import DetailArticleView from '@/views/DetailArticleView.vue'
import DetailQuestionView from '@/views/DetailQuestionView.vue'
import QuestionCreateView from '@/views/QuestionCreateView.vue'
import UpdateArticleView from '@/views/UpdateArticleView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/exchangerate',
      name: 'exchangerate',
      component: ExchangeRateView
    },
    {
      path: '/interestrate',
      name: 'interestrate',
      component: InterestRateView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: RecommendView
    },
    {
      path: '/board',
      name: 'board',
      component: BoardView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/profilechange/:conm',
      name: 'profilechange',
      component: ProfileChangeView
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: DepositView
    },
    {
      path: '/saving',
      name: 'saving',
      component: SavingView
    },
    {
      path: '/notice',
      name: 'notice',
      component: NoticeView
    },
    {
      path: '/faq',
      name: 'faq',
      component: FaqView
    },
    {
      path: '/questions',
      name: 'questions',
      component: QuestionView
    },
    {
      path: '/articles',
      name: 'articles',
      component: ArticleView
    },
    {
      path: '/createarticle',
      name: 'createarticle',
      component: ArticleCreateView
    },
    {
      path: '/detaildeposit/:conm',
      name: 'detaildeposit',
      component: DetailDepositView
    },
    {
      path: '/detailsaving/:conm',
      name: 'detailsaving',
      component: DetailSavingView
    },
    {
      path: '/articles/:id',
      name: 'DetailArticle',
      component: DetailArticleView
    },
    {
      path: '/questions/:id',
      name: 'DetailQuestion',
      component: DetailQuestionView
    },
    {
      path: '/createquestion',
      name: 'createquestion',
      component: QuestionCreateView
    },
    {
      path: '/updatearticle/:id',
      name: 'updatearticle',
      component: UpdateArticleView
    },
  ]
})

import { useFinanceStore } from '@/stores/finance'

router.beforeEach((to, from) => {
  const store = useFinanceStore()
  if (to.name === 'ArticleView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'HomeView' }
  }
})

export default router
