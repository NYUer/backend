from . import request
import time


class Core():

    TOKEN = ""
    CATE = {
        "course":   "course-catalog-exp/courses",
        "class":  "class-roster-exp/classes",
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
        getById = self.R.rawReq(self.CATE["faculty"] + "/users/nyu-ids/" + nyu_id, {})
        return getById

    def getRawClassesById(self, course_id):
        getById = self.R.rawReq(self.CATE["class"] + "?course_id=" + course_id, {})
        return getById

    def getRawCourses(self, keywords=""):
        getByTitle = self.R.rawReq(self.CATE["course"] + "?course_title=" + keywords + "&limit=15", {})
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
        
        getCalenders = self.R.rawReq(self.CATE["calendar"] +"?"+ param, {})
        return getCalenders
