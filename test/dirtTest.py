# coding=utf-8
class Dog(object):
    def __init__(self, name="sha", age=3, sex="公"):
        self.name = name
        self.age = age
        self.sex = sex


if __name__ == '__main__':
    d = {"name": "nini", "age": 3, "sex": "公"}
    person = {"name": "wowo", "age": 2, "dog": d}
    print person["name"]
    # print dog.name
    dog = person["dog"]
    print dog["name"]
    print dog["age"]
    print dog["sex"]
