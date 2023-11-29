<template>
  <div class="main_box">
    <!-- <div class="title">메인 페이지</div> -->
    <!-- 슬라이드 -->
    <div class="main_content">
    <div id="carouselExample" class="carousel slide">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="@/img/slide_1.png" class="d-block" alt="...">
        </div>
        <div class="carousel-item">
          <img src="@/img/slide_2.png" class="d-block" alt="...">
        </div>
        <!-- <div class="carousel-item">
          <img src="@/img/test111.jpg" class="d-block" alt="...">
        </div> -->
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
.main_box {
  display: flex;
  justify-content: center;
  width: 100%;
  margin: 0;
}

.main_content {
  /* width: 1200px; */
  width: 100%;
  justify-content: center;
  margin-bottom: 50px;
  z-index: 1;
  position: absolute;
}
.title {
  padding: 0 0 20px 10px;
}

.slide {
  position: relative;
  height: 767px;
}

.carousel-inner {
  height: 767px;
  position: relative;
  top: 0;
  left: 0;
  right: 0;
  background-size: cover;
  padding:0;
}

.carousel-item {
  height: 767px;
  position: absolute;
  padding:0;
}

.carousel-inner {
  height: 100%;
}

</style>