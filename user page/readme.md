## Base 구성들
### [ 프로젝트 구성 ]
- project
    - app

### [ 사이트 url ]
- /app
    - /index

### [ 적용된 기능들 ]
- templates 디렉토리에 템플릿 관리함
- 각 app별 urls을 별로도 관리함 (url include)
- static 디렉토리에서 스테틱 관리함

<br/>

## register/login 구성들
### [ 사이트 url ]
- /base
    - login
    - logout
    - register

### [ 사이트 forms ]
- form_errors : 필드 에러, 넌필드 에러

### [ 적용된 기능들 ]
- 로그인 시 -> url 이동 /
- 로그아웃 시 -> url 이동 /

<br/>

## user page 구성들
### [ 사이트 url ]
- /app
    - /index
    - /<int:pk> -> view.detail

### [ 적용된 기능들 ]
- 가입된 사용자 별 user page 생성
- 모든 템플릿 base.html 상속
- 네비게이션 바를 통해 로그인과 로그아웃 및 내 페이지 접근

### [ issue ]
- /app/<int:pk>로 이동 시에 해당 user pk로 자동으로 로그인됨
- nav바에 내 페이지로 이동하는거 안됨