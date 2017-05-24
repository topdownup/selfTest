# coding=utf-8
import mysql.connector
import ConfigParser


def getDatabaseConnector():
    try:
        conf = ConfigParser.ConfigParser()
        conf.read("../conf/database.conf")
        # print conf.get("user","database")
        # print conf.sections()
        # print conf.options("database")
        # print conf.get("database", "user")
        # print conf.items("database")
        # dict(conf.items("database"))
        config = dict(conf.items("database"))
        # conn = mysql.connector.connect(
        #         host=config["host"],
        #         port=config["port"],
        #         user=config["user"],
        #         password=config["password"],
        #         database=config["database"]
        # )
        conn = mysql.connector.connect(**config)
    except Exception, e:
        print "连接数据库异常，请检查配置"
    return conn


def with_connection(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__

        return func(*args, **kw)

    return wrapper


def insert(sql=""):
    try:
        conn = getDatabaseConnector()
        cur = conn.cursor()
        sql = "insert into demo_table (id,name,age) values (%(id)s,%(name)s,%(age)s);"
        par = (1, "ni", 20)
        count = cur.execute(sql, par)
        print "count=" + str(count)
        conn.commit()
        return count
    except Exception, e:
        print "rollback"
        if conn is not None:
            conn.rollback()
        print e.args
        print e
    finally:
        if cur is not None:
            cur.close
        if conn is not None:
            conn.close


def delete(sql="delete from demo_table where age<0;"):
    try:
        conn = getDatabaseConnector()
        cur = conn.cursor()
        # sql = "select id,prop_key,resource_id,text_value,user_id from properties;"
        count = cur.execute(sql)
        print "count=" + str(count)
        conn.commit()
        return count
    except Exception, e:
        print "rollback"
        if conn is not None:
            conn.rollback()
        print e.args
        print e
    finally:
        if cur is not None:
            cur.close
        if conn is not None:
            conn.close


def updata(sql="updata demo_table set age=-1 where age<0;"):
    try:
        conn = getDatabaseConnector()
        cur = conn.cursor()
        # sql = "select id,prop_key,resource_id,text_value,user_id from properties;"
        count = cur.execute(sql)
        print "count=" + str(count)
        res = cur.fetchall()
        for r in res:
            print r
        conn.commit()
        return res
    except Exception, e:
        print "rollback"
        if conn is not None:
            conn.rollback()
        print e.args
        print e
    finally:
        if cur is not None:
            cur.close
        if conn is not None:
            conn.close


def select(sql="select id,prop_key,resource_id,text_value,user_id from properties;"):
    try:
        conn = getDatabaseConnector()
        cur = conn.cursor()
        # sql = "select id,prop_key,resource_id,text_value,user_id from properties;"
        count = cur.execute(sql)
        print "count=" + str(count)
        res = cur.fetchall()
        for r in res:
            print r
        return res
    except Exception, e:
        print "rollback"
        if conn is not None:
            conn.rollback()
        print e.args
        print e
    finally:
        if cur is not None:
            cur.close
        if conn is not None:
            conn.close


if __name__ == "__main__":
    select()
