<template>
  <div class="articlelist" >
    <ArticleListItem
      v-for="(article, index) in store.articles"
      :key="article.id"
      :article="article"
      :index="index"
    />
  </div>
</template>

<script setup>
import { useFinanceStore } from '@/stores/finance'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useFinanceStore()
</script>

<style scoped>
.articlelist {
  color: black;
  text-decoration: none;
}
</style>