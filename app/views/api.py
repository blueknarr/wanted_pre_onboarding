from flask import Blueprint, jsonify, request
from app.models import JobPosting, Company, db
from sqlalchemy.exc import SQLAlchemyError


bp = Blueprint(
    'api',
    __name__,
    url_prefix='/application'
)


@bp.route('/register', methods=['POST'])
def register():
    """
    채용 공고를 등록하는 api
    기업명, 채용 직무, 보너스, 직무 설명서, 기술 스택을 입력받아
    db에 저장
    :return: dict
    """
    company_id = request.form['company_id']
    job_position = request.form['job_position']
    bonus = request.form['bonus']
    job_description = request.form['job_description']
    tech_stack = request.form['tech_stack']

    try:
        jp = JobPosting(
            company_id=company_id,
            job_position=job_position,
            bonus=bonus,
            job_description=job_description,
            tech_stack=tech_stack
        )

        db.session.add(jp)
        db.session.commit()
        return jsonify({'result': 'success'})
    except SQLAlchemyError as sqlerr:
        db.session.rollback()
        return jsonify({'result': 'failed', 'msg': sqlerr})


@bp.route('/update', methods=['POST'])
def update():
    """
    채용 공고 내용을 수정하는 api
    채용 공고 id로 해당하는 내용을 찾고
    채용 직무, 보너스, 직무 설명서, 기술 스택 변경 내용을 수정
    :return: dict
    """
    id = request.form['id']
    job_position = request.form['job_position']
    bonus = request.form['bonus']
    job_description = request.form['job_description']
    tech_stack = request.form['tech_stack']

    job_posting = JobPosting.query.get(id)

    if job_posting:
        try:
            job_posting.job_position = job_position
            job_posting.bonus = bonus
            job_posting.job_description = job_description
            job_posting.tech_stack = tech_stack

            db.session.add(job_posting)
            db.session.commit()
            return {'result': 'success'}
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'result': 'failed', 'msg': e})
    else:
        return {'result': 'failed', 'msg': f'{id}번 채용 공고가 없습니다.'}


@bp.route('/list', methods=['GET'])
def get_list():
    """
    채용 공고 목록을 보여주는 api
    :return: dict
    """
    job_postings = JobPosting.query.all()
    ret = []

    for job_posting in job_postings:
        company = Company.query.get(job_posting.company_id)

        ret.append({
            '채용공고': job_posting.id,
            '회사명': job_posting.company_id,
            '채용포지션': job_posting.job_position,
            '국가': company.country,
            '지역': company.region,
            '채용보상금': job_posting.bonus,
            '사용기술': job_posting.tech_stack
        })

    return jsonify(ret)