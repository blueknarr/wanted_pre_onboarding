from flask import Blueprint, jsonify, request
from app.models import JobPosting, Company, db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_
from sqlalchemy.orm import joinedload

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


@bp.route('/search', methods=['GET'])
def search():
    """
    키워드로 채용 공고를 검색하는 api
    category: 기업명, 기술 스택
    keyword: 검색어
    :return: dict
    """
    select = request.args.get('select')
    keyword = request.args.get('keyword')

    # 검색 수정
    if select == 'company_id':
        search_keywords = JobPosting.query.filter(
            JobPosting.company_id.ilike(f'%{keyword}%')
        ).all()
    elif select == 'tech_stack':
        search_keywords = JobPosting.query.filter(
            or_(
                JobPosting.tech_stack.ilike(f'%{keyword}%'),
                JobPosting.job_position.ilike(f'%{keyword}%')
            )
        ).all()

    if search_keywords:
        job_posting = []
        for search_keyword in search_keywords:
            job_posting.append({
                '채용공고': search_keyword.id,
                '회사명': search_keyword.company_id,
                '채용포지션': search_keyword.job_position,
                '국가': search_keyword.company.country,
                '지역': search_keyword.company.region,
                '채용보상금': search_keyword.bonus,
                '사용기술': search_keyword.tech_stack,
            })
        return jsonify(job_posting)
    else:
        return jsonify({'result': 'failed', 'msg': f'{keyword}에 해당하는 채용 공고가 없습니다.'})


@bp.route('/details', methods=['GET'])
def details():
    """
    채용 공고 상세 조회 api
    :return: dict
    """
    id = request.args.get('id')
    job_posting = JobPosting.query.options(joinedload(JobPosting.company)).filter(JobPosting.id == id).first()

    if job_posting:
        job_postings = JobPosting.query.filter(JobPosting.company_id == job_posting.company_id)

        job_posting_id = []
        for job_posting in job_postings:
            if int(id) == job_posting.id:
                continue
            job_posting_id.append(job_posting.id)

        ret = {
            '채용공고': job_posting.id,
            '회사명': job_posting.company_id,
            '채용포지션': job_posting.job_position,
            '국가': job_posting.company.country,
            '지역': job_posting.company.region,
            '채용보상금': job_posting.bonus,
            '채용내용': job_posting.job_description,
            '사용기술': job_posting.tech_stack,
            '다른 채용공고': job_posting_id
        }
        return ret
    else:
        return {'result': 'failed', 'msg': f'등록된 {id}번 채용 공고가 없습니다.'}