from . import request
import time


class Core():
    TOKEN = ""
    CATE = {
        "course": "course-catalog-exp/courses",
        "class": "class-roster-exp/classes",
        "calendar": "academic-calendar-exp/dates",
        "faculty": "faculty-exp"
    }
    TERM = {
        1: "JANUARY",
        5: "SPRING",
        8: "SUMMER",
        12: "FALL"
    }

    R = None

    def __init__(self, token):
        if not token:
            raise Exception("[Error] Token can not be empty!")

        self.TOKEN = token
        self.R = request.reqNYU(self.TOKEN)

    def getRawFacultyByNYUId(self, nyu_id):
        while 1:
            getById = self.R.rawReq(self.CATE["faculty"] + "/users/nyu-ids/" + nyu_id, {})
            if isinstance(getById, list):
                break
        return getById

    def getRawFacultyByKeyword(self, keyword):
        keyword = keyword.split()
        rsp = {}
        for word in keyword:
            while 1:
                class_list = self.getRawClassesByInstuctor(word)
                if isinstance(class_list, list):
                    break
            for session in class_list:
                instructor_nyuid = session["instructor_nyu_id"]
                if instructor_nyuid not in rsp:
                    rsp[instructor_nyuid] = dict(instructor_nyu_id=session["instructor_nyu_id"],
                                                 instructor_role_description=session["instructor_role_description"],
                                                 instructor_name=session["instructor_name"])
        rsp = list(rsp.values())
        return rsp

    def getRawClassesByInstuctor(self, keyword):
        while 1:
            getById = self.R.rawReq(self.CATE["class"] + "?instructor_name=" + keyword, {})
            if isinstance(getById, list):
                break
        return getById

    def getRawClassesById(self, course_id):
        while 1:
            getById = self.R.rawReq(self.CATE["class"] + "?course_id=" + course_id, {})
            if isinstance(getById, list):
                break
        return getById

    def getRawCourses(self, keywords=""):
        while 1:
            getByTitle = self.R.rawReq(self.CATE["course"] + "?course_title=" + keywords + "&limit=50", {})
            if isinstance(getByTitle, list):
                break
        return getByTitle

    def getRawCalenders(self, date="", term=None):
        # date = time.strftime('%Y/%m/%d',time.localtime())
        param = ""
        if date:
            param = "start_date=" + date
        elif not date and term == None:
            currentMonth = time.localtime()[1]
            for month in self.TERM:
                term = self.TERM[month]
                if month >= currentMonth:
                    break

            param = "term=" + term + "-" + str(time.localtime()[0])
        else:
            param = "term=" + term

        getCalenders = self.R.rawReq(self.CATE["calendar"] + "?" + param, {})
        return getCalenders
