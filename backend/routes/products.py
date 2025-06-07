from flask import Blueprint, request, jsonify
from utils.db import get_db

bp = Blueprint('products', __name__, url_prefix='/api/products')

@bp.route('/search', methods=['GET'])
def search():
    q = request.args.get('q', '')
    print("Received search query:", q)
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM products
        WHERE name LIKE %s OR category LIKE %s
    """, (f'%{q}%', f'%{q}%'))
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in rows]
    return jsonify(results)


