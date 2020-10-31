#coding:utf-8
import pytest

#@pytest.mark.usefixtures('login')
@pytest.fixture(scope='class')
def login():
    print("登录操作")
    yield
    print('登出')

class Test1:
    def test_case1(self,login):
        print("用例1")

# def test_case2():
#     print("用例2")
#
# def test_case3(conn_db):
#     print(conn_db)
#     print('用例3')