# 프리온보딩 백엔드 코스 3차 선발과제

- 기업의 채용을 위한 웹 서비스 입니다. 
- 채용공고를 생성하고, 이에 사용자는 지원합니다

<br>

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



## 데이터 베이스

### ERD

- company: 기업 정보(기업명, 국가, 지역)
- job_posting: 채용 공고(id, 채용 기업, 직무, 보너스, 직무 설명서, 기술 스택)
- application_history: 채용 공고 지원 내역(id, 채용공고 id, 유저 id)
- users: 사용자(id)

![erd](https://user-images.githubusercontent.com/44389424/174472522-ec40a494-f91e-4df2-9905-18224f1b4e29.png)

## API

API 사용법을 안내합니다.



### 채용공고 등록하기 

채용 공고를 등록합니다. 기업명, 채용 직무, 보너스, 직무 설명서, 기술 스택을  `POST`로 요청하고, 성공 시 응답 바디에 `JSON` 객체로 성공 메세지를 받습니다. 실패 시 에러 코드를  받습니다.



#### Request

##### URL

```http
POST /application/register HTTP/1.1
Host: 127.0.0.1:5000
```

##### Parameter

| Name            | Type       | Description | Required |
| :-------------- | :--------- | :---------- | :------- |
| company_id      | `String`   | 회사명      | O        |
| job_position    | `String`   | 채용 포지션 | O        |
| bonus           | `Int`      | 채용 보상금 | O        |
| job_description | ``String`` | 업무 소개   | O        |
| tech_stack      | `String`   | 사용 기술   | O        |



#### Response

| Name   | Type     | Description      |
| :----- | :------- | :--------------- |
| result | `String` | 등록 결과 메세지 |



#### Result

##### Response:성공

```json
{
  "result": "success"
}
```

##### Response:실패

```json
{
  "result": "failed"
}
```



### 채용공고 수정하기 

채용 공고를 수정합니다. 채용 공고 id, 채용 직무, 보너스, 직무 설명서, 기술 스택을  `POST`로 요청하고, 성공 시 응답 바디에 `JSON` 객체로 성공 메세지를 받습니다. 실패 시 에러 코드를  받습니다.



#### Request

##### URL

```http
POST /application/update HTTP/1.1
Host: 127.0.0.1:5000
```

##### Parameter

| Name            | Type       | Description  | Required |
| :-------------- | :--------- | :----------- | :------- |
| id              | `String`   | 채용 공고 id | O        |
| job_position    | `String`   | 채용 포지션  | O        |
| bonus           | `Int`      | 채용 보상금  | O        |
| job_description | ``String`` | 업무 소개    | O        |
| tech_stack      | `String`   | 사용 기술    | O        |



#### Response

| Name   | Type     | Description      |
| :----- | :------- | :--------------- |
| result | `String` | 등록 결과 메세지 |



#### Result

##### Response:성공

```json
{
  "result": "success"
}
```

##### Response:실패

```json
{
    "result": "failed",
    "msg": "{id}번 채용 공고가 없습니다."
}
```



### 채용공고 조회하기 

채용 공고를 조회합니다. `GET`으로 요청하면, 성공 시 응답 바디에 `JSON` 객체로 성공 메세지를 받습니다. 실패 시 에러 코드를  받습니다.



#### Request

##### URL

```http
GET /application/list HTTP/1.1
Host: 127.0.0.1:5000
```



#### Response

| Name         | Type     | Description  |
| :----------- | :------- | :----------- |
| country      | `String` | 국가         |
| tech_stack   | `String` | 사용 기술    |
| region       | `String` | 지역         |
| id           | `String` | 채용 공고 id |
| bonus        | `Int`    | 채용보상금   |
| job_position | `String` | 채용 포지션  |
| company_id   | `String` | 회사명       |



#### Result

##### Response:성공

```json
[
    {
        "국가": "한국",
        "사용기술": "react, redux",
        "지역": "판교",
        "채용공고": 2,
        "채용보상금": 3000,
        "채용포지션": "프론트엔드 개발자",
        "회사명": "카카오"
    },
    {
        "국가": "한국",
        "사용기술": "python, django",
        "지역": "판교",
        "채용공고": 3,
        "채용보상금": 2000,
        "채용포지션": "백엔드 개발자",
        "회사명": "카카오 뱅크"
    },
    {
        "국가": "한국",
        "사용기술": "java, spring",
        "지역": "정자",
        "채용공고": 4,
        "채용보상금": 10000,
        "채용포지션": "백엔드 개발자",
        "회사명": "네이버"
    },
    {
        "국가": "한국",
        "사용기술": "python",
        "지역": "서울",
        "채용공고": 1,
        "채용보상금": 900,
        "채용포지션": "Django 백엔드 주니어 개발자",
        "회사명": "원티드랩"
    }
]
```



### 채용공고 검색하기 

채용 공고를 검색합니다. 카테고리, 키워드를  `GET`으로 요청하고, 성공 시 응답 바디에 `JSON` 객체로 성공 메세지를 받습니다. 실패 시 에러 코드를  받습니다.



#### Request

##### URL

```http
GET /application/search?select={category}&keyword={keyword} HTTP/1.1
Host: 127.0.0.1:5000
```

##### Parameter

| Name    | Type     | Description                      | Required |
| :------ | :------- | :------------------------------- | :------- |
| select  | `String` | 카테고리: company_id, tech_stack | O        |
| keyword | `String` | 검색 키워드                      | O        |



#### Response

| Name         | Type     | Description  |
| :----------- | :------- | :----------- |
| country      | `String` | 국가         |
| tech_stack   | `String` | 사용 기술    |
| region       | `String` | 지역         |
| id           | `String` | 채용 공고 id |
| bonus        | `Int`    | 채용보상금   |
| job_position | `String` | 채용 포지션  |
| company_id   | `String` | 회사명       |



#### Result

##### Response:성공 (category: tech_stack, keyword: python)

```json
[
    {
        "국가": "한국",
        "사용기술": "python, django",
        "지역": "판교",
        "채용공고": 3,
        "채용보상금": 2000,
        "채용포지션": "백엔드 개발자",
        "회사명": "카카오 뱅크"
    },
    {
        "국가": "한국",
        "사용기술": "python",
        "지역": "서울",
        "채용공고": 1,
        "채용보상금": 900,
        "채용포지션": "Django 백엔드 주니어 개발자",
        "회사명": "원티드랩"
    }
]
```

##### Response:실패

```json
{
    "result": "failed",
    "msg": "{keyword}에 해당하는 채용 공고가 없습니다."
}
```



### 채용공고 상세 정보 조회하기 

채용 공고 상세 정보를 조회합니다. `GET`으로 요청하면, 성공 시 응답 바디에 `JSON` 객체로 성공 메세지를 받습니다. 실패 시 에러 코드를  받습니다.



#### Request

##### URL

```http
GET /application/details?id={id} HTTP/1.1
Host: 127.0.0.1:5000
```

##### Parameter

| Name | Type  | Description  | Required |
| :--- | :---- | :----------- | :------- |
| id   | `Int` | 채용 공고 id | O        |



#### Response

| Name           | Type     | Description                |
| :------------- | :------- | :------------------------- |
| country        | `String` | 국가                       |
| job_posting_id | `LIST`   | 동일 회사명 다른 채용 공고 |
| tech_stack     | `String` | 사용 기술                  |
| region         | `String` | 지역                       |
| id             | `String` | 채용 공고 id               |
| bonus          | `Int`    | 채용보상금                 |
| job_position   | `String` | 채용 포지션                |
| company_id     | `String` | 회사명                     |



#### Result

##### Response:성공

```json
{
    "국가": "한국",
    "다른 채용공고": [
        5
    ],
    "사용기술": "python, Node.js",
    "지역": "서울",
    "채용공고": 5,
    "채용내용": "프리온보딩 백엔드 코스 참여 교육생 모집",
    "채용보상금": 0,
    "채용포지션": "프리온보딩 백엔드 코스",
    "회사명": "원티드랩"
}
```

##### Response:실패

```json
{
    "result": "failed",
    "msg": "등록된 {id}번 채용 공고가 없습니다."
}
```



### 채용공고 지원하기 

채용 공고에 지원합니다.  `POST`로 요청하고, 성공 시 응답 바디에 `JSON` 객체로 성공 메세지를 받습니다. 실패 시 에러 코드를  받습니다.



#### Request

##### URL

```http
POST /application/apply HTTP/1.1
Host: 127.0.0.1:5000
```

##### Parameter

| Name           | Type     | Description  | Required |
| :------------- | :------- | :----------- | :------- |
| job_posting_id | `String` | 채용 공고 id | O        |
| user_id        | `String` | 유저 id      | O        |



#### Response

| Name   | Type     | Description      |
| :----- | :------- | :--------------- |
| result | `String` | 등록 결과 메세지 |



#### Result

##### Response:성공

```json
{
    "result": "success"
}
```

##### Response:실패

```json
{
    "result": "failed",
    "msg": "지원을 완료한 채용 공고입니다."
}
```



### 채용공고 삭제하기 

채용 공고를 삭제합니다.  `GET`으로 요청하고, 성공 시 응답 바디에 `JSON` 객체로 성공 메세지를 받습니다. 실패 시 에러 코드를  받습니다.



#### Request

##### URL

```http
GET /application/delete?id={id} HTTP/1.1
Host: 127.0.0.1:5000
```

##### Parameter

| Name | Type     | Description  | Required |
| :--- | :------- | :----------- | :------- |
| id   | `String` | 채용 공고 id | O        |



#### Response

| Name   | Type     | Description      |
| :----- | :------- | :--------------- |
| result | `String` | 등록 결과 메세지 |



#### Result

##### Response:성공

```json
{
    "result": "success",
    "msg": "{id}번 채용 공고를 삭제했습니다.",
}
```

##### Response:실패

```json
{
    "result": "failed",
    "msg": "{id}번 채용 공고가 없습니다."
}
```

