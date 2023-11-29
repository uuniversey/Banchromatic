<template>
  <div class="board_box">
    <div class="title">✏ 공지사항</div>
    <div class="content">
      <RouterLink :to="{name: 'notice'}">공지사항</RouterLink>  |
      <RouterLink :to="{name: 'faq'}">자주 묻는 질문</RouterLink> |
      <!-- <RouterLink :to="{name: 'questions'}">Q&A</RouterLink> | -->
      <RouterLink :to="{name: 'articles'}">금융 상품 후기</RouterLink>
    </div>
  </div>
  <div class="faq_1">
  <div class="faq">
      <!-- <div>
        <button type="button" class="question isActive" @click="showAnswer">Q . 질문</button>
        <div class="answer">A . 답변</div>
        <hr>
        <button type="button" class="question">c</button>
        <hr>
        <button type="button" class="question">Q . 질문</button>
        <hr>
      </div> -->
      <div class="accordion accordion-flush" id="accordionFlushExample">
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
            <p>2023.11.23</p> [공지] 상품가입서비스 이용약관 개정 안내
          </button>
        </h2>
        <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
          <div class="accordion-body">상품가입서비스 이용약관이 새롭게 변경됩니다.<br>변경되는 내용을 안내드리오니 서비스 이용에 참고하시기 바랍니다.<br><br>1. 주요 개정사항
            <br>- 주택담보대출 및 전세대출 관련 대출이동시스템 내용 추가<br>...</div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
            <p>2023.11.21</p> [공지] 시스템 점검 안내
          </button>
        </h2>
        <div id="flush-collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
          <div class="accordion-body">안녕하세요. - 입니다.<br> ~ 시스템 점검으로 아래 시간 동안 ~ 이용이 제한 됩니다.
            <br><br><strong>[이용 제한 시간]</strong><br>2023.11.22(수) 02:00 ~ 2023.11.22(수) 06:00<br> ...</div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
            <p>2023.11.18</p> [공지] 개인정보처리방침 개정 안내
          </button>
        </h2>
        <div id="flush-collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
          <div class="accordion-body">- 개인정보처리방침이 새롭게 변경됩니다.
            <br>-는 이용자 여러분의 개인정보를 소중하게 처리하고 있으며, 안전하게 관리하고 있습니다.<br>
              새롭게 바뀐 개인정보처리방침의 주요 변경사항을 확인하시고 서비스 이용에 참고하시기 바랍니다.<br>
              <br>1. 변경사항
              <br>- 개인정보 수집항목 및 목적 최신화
              <br>- 개인정보 위탁 현황 및 제3자 제공 현황 현행화
              <br>- 법적 필수 고지항목 정비
              <br>...</div>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style scoped>
.board_box {
  margin: 20px 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.title {
  font-weight: bold;
  font-size: 25px;
  margin-bottom: 20px;
  text-align: center;
}
.content {
  text-align: center;
  /* display: flex; */
  justify-content: center;
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
  padding-left: 120px;
}

p {
  margin: 10px 20px 10px 0;
  color: #acacac;
}
</style>