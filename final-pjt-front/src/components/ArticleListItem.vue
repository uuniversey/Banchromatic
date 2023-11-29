<template>
  <div class="article_item">
  <RouterLink  style="text-decoration: none" :to="{name : 'DetailArticle', params: {id: article.id}}">
  <div class="article">
    <p>{{ index+1 }}</p>
    <p>{{ article.title }}</p>
    <p>{{ article.user.username }}</p>
  </div>
  </RouterLink>
  </div>
  <hr>
</template>

<script setup>

defineProps({
  article: Object,
  index: Number
})

</script>

<style scoped>
.article_item {
  padding: 0 50px;
  height: 20px;
}

.article {
  text-decoration: none;
  display: flex;
  justify-content: space-between;
  color: black;
}

</style>