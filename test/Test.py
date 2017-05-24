# coding=utf-8
class Student(object):
    age = 0

    def __init__(self, name="wowo"):
        self.__name = name

    @property
    def name(self):
        print "调用了get"
        return self.__name

    @name.setter
    def name(self, value):
        print "调用了set"
        self.__name = value


if __name__ == "__main__":
    try:
        s = Student()
        print s.name
        s.name = None
        print s.name + ""
        print ""
        print "23232323"
    except Exception, e:
        print e.message
    finally:
        print "finally"
