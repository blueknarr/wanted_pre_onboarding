from app import db
from app.models import Company, JobPosting, Users

# company 테이블
wanted_lab = Company(id='원티드랩', country='한국', region='서울')
kakao = Company(id='카카오', country='한국', region='판교')
kakao_bank = Company(id='카카오 뱅크', country='한국', region='판교')
naver = Company(id='네이버', country='한국', region='정자')
db.session.add(wanted_lab)
db.session.add(kakao)
db.session.add(kakao_bank)
db.session.add(naver)

# users 테이블
iu = Users(id='아이유')
winter = Users(id='윈터')
db.session.add(iu)
db.session.add(winter)

# job_posting 테이블
wanted_lab_jp = JobPosting(company_id='원티드랩', job_position='Django 백엔드 주니어 개발자', bonus=1000, job_description='백엔드 개발자 신입 및 인턴', tech_stack='python')
wanted_lab_jp_2 = JobPosting(company_id='원티드랩', job_position='프리온보딩 백엔드 코스', bonus=0, job_description='프리온보딩 백엔드 코스 참여 교육생 모집', tech_stack='python, Node.js')
kakao_jp = JobPosting(company_id='카카오', job_position='프론트엔드 개발자', bonus=3000, job_description='프론트엔드 개발자 경력 3년', tech_stack='react, redux')
kakao_bank_jp = JobPosting(company_id='카카오 뱅크', job_position='백엔드 개발자', bonus=2000, job_description='백엔드 개발자 경력 2년', tech_stack='python, django')
naver_jp = JobPosting(company_id='네이버', job_position='백엔드 개발자', bonus=10000, job_description='백엔드 개발자 경력 10년', tech_stack='java, spring')
db.session.add(wanted_lab_jp)
db.session.add(wanted_lab_jp_2)
db.session.add(kakao_jp)
db.session.add(kakao_bank_jp)
db.session.add(naver_jp)

db.session.commit()