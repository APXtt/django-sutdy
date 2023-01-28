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