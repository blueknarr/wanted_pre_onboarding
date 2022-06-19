# wanted_pre_onboarding
프리온보딩 백엔드 코스 3차 선발과제



## 개발환경

### Version

- python 가상 환경 (3.8 버전+)
- PostgreSQL (14.4)

### 패키지 설치

```
$ poetry update
```

### env.py

```
DB_NAME='test'
DB_USER='postgres'
DB_HOST='localhost'
DB_PASSWORD='postgres'
DB_PORT='5432'
```

### 데이터베이스 초기화하기

```
$ flask db init
$ flask db migrate
$ flask db upgrate
```

### flask 실행

```
$ flask run
```

### 

## 데이터 베이스

### ERD

- company: 기업 정보(기업명, 국가, 지역)
- job_posting: 채용 공고(id, 채용 기업, 직무, 보너스, 직무 설명서, 기술 스택)
- application_history: 채용 공고 지원 내역(id, 채용공고 id, 유저 id)
- users: 사용자(id)