import cx_Oracle                                                #引用模块cx_Oracle

class PyOracle():
    def __init__(self,username,passwd,url):
        self.__username = username
        self.__passwd = passwd
        self.__url = url
        conUrl = username + "/" + passwd + "@" + url
        self.con = cx_Oracle.connect(conUrl)



if __name__ == '__main__':
    connection = PyOracle("C##nibudon","123456","127.0.0.1:1521/orcl").con
    cursor = connection.cursor()
    sql = "select * from t_user"
    cursor.execute(sql)
    result = cursor.fetchone()
    while result:
        print(result)
        result = cursor.fetchone()
    cursor.close()
    connection.close()