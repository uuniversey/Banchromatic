<template>
  <div class="inter_box">
    <div class="inter_nav">
    <div class="title">금리 비교</div>
    <RouterLink :to="{ name: 'deposit' }">정기예금</RouterLink> |
    <RouterLink :to="{ name: 'saving' }">정기적금</RouterLink>
  </div>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>
.inter_box {
  display: flex;
  justify-content: center;
  margin-top: 30px;
}
.inter_nav {
  width: 1200px;
  margin-left: 20px;
}

.title {
  padding: 0 0 20px 0;
  font-weight: bold;
  font-size: 20px;
}

a {
  text-decoration: none;
}

a:visited {
  color:black
}
</style>