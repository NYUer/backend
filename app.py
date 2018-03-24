from flask import Flask, request, jsonify
from nyuapi import SP
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = SP("12c4b1b3-6e1b-3491-9b9f-14cf3d612045")


@app.route('/course', methods=['GET'])
def search_course():
    keyword = request.args.get('keyword')
    rsp = api.getRawCourses(keyword)
    return jsonify(rsp)


@app.route('/class', methods=['GET'])
def search_class():
    keyword = request.args.get('course_id')
    raw_rsp = api.getRawClassesById(keyword)
    rsp = {}
    for session in raw_rsp:
        faculty_nid = session["instructor_nyu_id"]
        if faculty_nid not in rsp:
            new_faculty = dict(instructor_nyu_id = session["instructor_nyu_id"],
                               instructor_role_description = session["instructor_role_description"],
                               instructor_name = session["instructor_name"]
                               )
            rsp[faculty_nid] = new_faculty
    return jsonify(rsp)


@app.route('/faculty', methods=['GET'])
def search_faculty():
    keyword = request.args.get('instructor_nyu_id')
    rsp = api.getRawFacultyByNYUId(keyword)
    return jsonify(rsp)


if __name__ == '__main__':
    app.run()
