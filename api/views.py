from flask import jsonify, Blueprint

from dao.dao import PostDAO
import logging, datetime


api_blueprint = Blueprint('api_blueprint', __name__)
posts = PostDAO('./data/posts.json', './data/comments.json')
logging.basicConfig(filename='./logs/basic.log', level=logging.INFO)

@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    logging.info(f'{datetime.datetime.now()} [INFO] Запрос /api/posts/')
    res = posts.load_posts()
    return jsonify(posts.load_posts())


@api_blueprint.route('/api/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    logging.info(f'{datetime.datetime.now()} [INFO] Запрос /api/posts/{postid}')
    return jsonify(posts.get_post_by_pk_json(postid))