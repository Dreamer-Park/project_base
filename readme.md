## Backend for people_on_the_road

### Requirement & SCOPE
- 지도 예약기능
- 지도 검색기능
- 게시판 기능 (CRUD)
- 블로그 기능 (CRUD)
- DB 및 보안 관리
- 외부 미디어 파일 확인 및 조회기능 
(1차적으로 클라우드 서비스 권한관리를 통해서 사용해보자 구현 순위 낮음)
- 세션관리 (최소 세션은 1시간 => 해당 로그는 보존되어야함, 업로드 등의 활동이 진행되면 유지될 것)
- 관리자용 홈페이지를 따로 만들 것이 아닌 django admin 를 그대로 사용
(필요한 내용은 iframe으로 적용할 필요성이 있음)
- 결제관련



### ver 0.1
- Setting의 분리 (production 과 development의 분리) 및 vscode launch에 등록 runserver 및 shell 명령어는 아래로 사용 
https://cjh5414.github.io/django-settings-separate/
- API KEY 등록 / NAVER / kaako / GOOGLE / OPENAPI 을 위한 모델 생성 (외부 api용 환경 구축)
- social login 구현
GOOGLE :
Facebook :
Twitter : 
NAVER :
KAKAO :
QQ : https://janrain-education-center.knowledgeowl.com/home/qq-social-login-configuration-guide

### Gitignore
./secret/ 에 json형태로 보관 추후 환경변수 형태로 관리 필요
## 비고 secret 키는?
- django.contrib.sessions.backends.cache 이외의 session backend를 사용하고 있거나,
- 기본 get_session_auth_hash()를 사용하는 모든 sessions
- CookieStorage 혹은 FallbackStorage 를 사용하는 모든 messages
- 모든 PasswordResetView
- 다른 키가 제공되지 않는 암호화 서명 사용 시 사용된다.

