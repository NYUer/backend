from flask import Flask, request, jsonify
from nyuapi import SP
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = SP("37e6a77d-fa69-3b5b-97a3-6fe4fe52b9ff")


@app.route('/course', methods=['GET'])
def search_course():
    keyword = request.args.get('keyword')
    rsp = api.getRawCourses(keyword)
    count = 0
    for course in rsp:
        if count > 10:
            break
        spec_rsp = api.getRawClassesById(course['course_id'])
        count += 1
        if spec_rsp:
            course['course_title'] = spec_rsp[0]['nyu_course_id'] + ": " + course['course_title']
            course['location_description'] = spec_rsp[0]['location_description']
        else:
            course['location_description'] = "N/A"
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
    nyu_id = request.args.get('instructor_nyu_id')
    keyword = request.args.get('keyword')
    if keyword is None:
        rsp = api.getRawFacultyByNYUId(nyu_id)
    else:
        rsp = api.getRawFacultyByKeyword(keyword)
    return jsonify(rsp)


if __name__ == '__main__':
    app.run("0.0.0.0", 80, threaded=True)
