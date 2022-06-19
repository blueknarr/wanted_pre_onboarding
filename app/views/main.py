from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return '프리온보딩 백엔드 코스 3차 선발과제'