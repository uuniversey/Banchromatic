<template>
  <div class="board_box">
    <div class="title">✏ 자주 묻는 질문</div>
    <div class="content">
      <RouterLink :to="{name: 'notice'}">공지사항</RouterLink>  |
      <RouterLink :to="{name: 'faq'}">자주 묻는 질문</RouterLink> |
      <!-- <RouterLink :to="{name: 'questions'}">Q&A</RouterLink> | -->
      <RouterLink :to="{name: 'articles'}">금융 상품 후기</RouterLink>
    </div>
  </div>
  <div class="faq_1">
  <div class="faq">
      <div class="accordion accordion-flush" id="accordionFlushExample">
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
            Q . 질문
          </button>
        </h2>
        <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
          <div class="accordion-body">A . 답변</div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
            Q . 질문
          </button>
        </h2>
        <div id="flush-collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
          <div class="accordion-body">A . 답변</div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
            Q . 질문
          </button>
        </h2>
        <div id="flush-collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
          <div class="accordion-body">A . 답변</div>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isActive: false,
    }
  }
}

function showAnswer() {
  var before = document.getElementsByClassName('isActive')[0];
  if (before && document.getElementsByClassName('isActive')[0] !=  this){
    before.nextElementSibling.style.maxHeight = null;
    before.classList.remove('isActive');
  }
  this.classList.toggle('isActive');

  var content = element.nextElementSibling
  if (content.style.maxHeight != 0) {
    content.style.maxHeight = null;
  } else {
    content.style.maxHeight = content.scrollHeight + 'px';
  }
}


</script>

<style scoped>
.board_box {
  margin: 20px 0;
}
.title {
  font-weight: bold;
  font-size: 25px;
  margin-bottom: 20px;
  text-align: center;
}
.content {
  text-align: center;
  
}
.content a {
  text-decoration: none;
  color: black;
  padding: 20px;
}

.faq_1 {
  justify-content: center;
  display: flex;
}
.faq {
  width: 1200px;
  justify-content: center;
}

.question {
  background-color: #eee;
  color: #444;
  cursor: pointer;
  padding: 18px;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}
.active, .question:hover {
  background-color: #555;
}
.answer {
  padding: 18px;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  display: none;
}

hr {
  padding: 0;
  margin: 0;
}
.accordion-body {
  padding-left: 70px;
}

.accordion-header {
  padding: 0 50px;
  margin: 10px 0;
}
</style>