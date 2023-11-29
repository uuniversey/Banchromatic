
### 금융 상품 비교 웹

# Banchromatic

### 목차
1. [프로젝트 기간](#1-프로젝트-기간)
2. [사용한 기술 스택](#2-사용한-기술-스택)
3. [팀원 정보 및 업무 분담 내역](#3-팀원-정보-및-업무-분담-내역)
4. [설계 내용 및 실제 구현 정도](#4-설계-내용-및-실제-구현-정도)
5. [데이터베이스 모델링](#5-데이터베이스-모델링)
6. [금융 상품 추천 알고리즘에 대한 설명](#6-금융-상품-추천-알고리즘에-대한-설명)
7. [서비스 대표 기능들에 대한 설명](#7-서비스-대표-기능들에-대한-설명)
8. [느낀 점 및 후기](#8-느낀-점-및-후기)

<br><br>
----
### 1. 프로젝트 기간
  - 2023.11.16 ~ 2023.11.24

<br><br>
----
### 2. 사용한 기술 스택
  - front
    * javascript
    * vue.js
    * bootstrap
    
  - back
    * python
    * django

<br><br>
----
### 3. 팀원 정보 및 업무 분담 내역
  - 이우주 
    * 회원 커스터마이징 기능 구현
    * 예적금 금리 비교 기능 구현
    * 환율 계산기 구현
    * 프로필 페이지 구현

  - 이윤정
    * 메인 페이지 구현
    * 근처 은행 검색 기능 구현
    * 커뮤니티 기능 구현
    * 프론트 css 제작
    
<br><br>
----
### 4. 설계 내용 및 실제 구현 정도
  - 메인 페이지
    - Carousel을 사용한 메인 페이지 구성

  - 회원 커스터마이징
    - 회원 관리 라이브러리(allauth & dj-rest-auth) 등을 사용하여 회원 관리기능 구성
    - Django의 커스텀 User를 활용하기 위해 적절한 Serializer를 구성
    - 회원 정보와 가입한 상품 목록을 n:m 관계로 모델링하여 활용  

  - 예적금 금리 비교
    - 금융상품통합비교공시 api를 활용하여 금융 상품 정보를 가져와 db에 저장
    - db에 이미 저장한 데이터는 새로 저장하지 않고 변경사항만을 수정하도록 구성
    - 예금/적금 각각의 상품 목록을 개월 수 기준으로 볼 수 있도록 화면 구성
    - 은행을 선택하여 목록을 필터링 할 수 있도록 구성
    - 특정 상품을 클릭 시 상세 정보를 볼 수 있는 페이지 구성성
    - 가입하기/해지하기 버튼을 추가하여 회원 정보에 가입한 상품 목록을 추가/제거 할 수 있도록 구성 (로그인 된 사용자만 이용 가능)

  - 환율 계산기
    - 한국수출입은행 환율정보 api를 활용하여 현재 환율에 대한 정보를 가져와 db에 저장
    - 두 개의 국가를 선택하여 환율을 계산할 수 있도록 구성
  
  - 근처 은행 검색
    - kakao maps api를 활용하여 페이지에 지도를 표시
    - 위치와 은행을 선택하여 근처의 은행 정보를 출력 할 수 있게 구성

  - 커뮤니티
    - 회원간 소통 할 수 있는 커뮤니티 기능 구현
    - 게시글 조회, 생성, 수정, 댓글 생성 및 삭제 기능 구현
  
  - 프로필 페이지
    - 회원의 기본 정보를 출력 할 수 있도록 화면을 구성
    - 회원 정보를 수정하기 위한 화면을 구성
    - 가입한 금융 상품 리스트를 출력 할 수 있도록 화면을 구성

  - 금융 상품 추천 알고리즘
    - 은행명과 저축 기간 및 저축 금액을 선택하여 그에 맞는 상품을 추천 받을 수 있도록 구성
    - 추천 받기 버튼을 추가하여 추천 상품 목록을 보여주고 그 중 베스트 상품과 베스트 상품의 이율을 보여주도록 구성

<br><br>
----
### 5. 데이터베이스 모델링

  ![img](final-pjt-front/src/img/erd.png)


<br><br>
----
### 6. 금융 상품 추천 알고리즘에 대한 설명
  - 유저에게 원하는 은행명과 저축 기간을 받는다.
  - 받은 은행명에 해당하는 모든 예/적금 상품을 탐색하여 담아 놓는다.
  - 담아 놓은 정보에서 고유한 값인 상품코드를 뽑아 예/적금 옵션 데이터를 탐색하며 상품 코드가 일치하면서 동시에 유저에게 받은 저축 기간과 일치하는 상품을 담아 추천 상품 목록에 보여준다.
  - 만들어진 추천 상품 목록에서 가장 큰 이율을 가진 상품을 추천해주고 그 이율을 화면에 보여준다.

<br><br>
----
### 7. 서비스 대표 기능들에 대한 설명
  - 환율 계산 기능을 한국 원을 기준으로 하는 것 뿐 아니라 원하는 두 국가 간의 환율 계산을 해 줄 수 있는 기능으로 제작하였다.
  
  - 원하는 통화의 정보를 볼 수 있는 카드를 구성하였다.

  - 금융 상품을 여러개 추천해 줄 뿐 아니라 그 중 가장 좋은 이율을 가진 상품을 보여준다.

  - 게시판에서 아코디언을 활용해서 자주 묻는 질문과 공지사항을 깔끔하게 보여준다.

  - 프로필 페이지에서 예/적금 가입 정보를 보여주고 그 자리에서 바로 상세 정보를 볼 수 있게 하여 가입/해지가 쉽게 구성하였다.

<br><br>
----
### 8. 느낀 점 및 후기
  - 협업을 본격적으로 진행하며 branch 설정 및 git merge에 대한 개념에 대해 확실하게 이해 할 수 있게 되었다.

  - axios를 활용해서 back과 front 간에 정보를 crud 하는 것에 익숙해 질 수 있었다.

  - 본격적인 시작을 하기 전에 db를 보다 효율적으로 활용하기 위한 modeling에 대해 고민해 봐야겠다는 것을 느꼈고 1:N, N:M 관계를 활용해 보며 데이터를 다루는 것에 더 익숙해져야 한다고 생각한다.

  - 다음 프로젝트에선 더 다양한 api를 활용하여 풍성한 웹페이지를 만들어 보고 싶다.

  - 기능이 추가 될수록 원하는 기능이 있는 페이지를 찾기가 힘들어져 vue.js의 views와 component를 네이밍 및 정리까지 생각해서 효율적으로 관리하는 법을 고민해 봐야겠다.
