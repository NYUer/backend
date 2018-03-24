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
    rsp = api.getRawClassesById(keyword)
    return jsonify(rsp)


@app.route('/faculty', methods=['GET'])
def search_faculty():
    keyword = request.args.get('instructor_nyu_id')
    rsp = api.getRawFacultyByNYUId(keyword)
    return jsonify(rsp)


if __name__ == '__main__':
    app.run()
