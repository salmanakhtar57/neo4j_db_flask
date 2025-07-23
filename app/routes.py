from flask import Blueprint, render_template, jsonify
from app.models import Token, Project, File, User

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    try:
        tokens = [token.name for token in Token.nodes.all()]
        projects = [project.name for project in Project.nodes.all()]
        
        # Fetch files in Project 1
        project1 = Project.nodes.get(name="AI Analytics Platform")
        files_in_project_1 = [f.filename for f in project1.files.all()]
        
        # Images with width=200 by google_id user
        user = User.nodes.get(google_id="102718630068735143796")
        images = [
            {"filename": f.filename, "width": f.width}
            for f in user.uploads.filter(width=200)
        ]
        
        data = {
            'tokens': tokens,
            'projects': projects,
            'files_in_project_1': files_in_project_1,
            'images_by_google_user': images
        }
        return render_template('index.html', data=data)
    except Exception as e:
        return render_template('index.html', error=str(e)), 500

@bp.route('/api/data')
def api_data():
    try:
        response = {
            'status': 'success',
            'tokens': ['Token A', 'Token B'],
            'projects': ['Project 1', 'Project 2'],
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
