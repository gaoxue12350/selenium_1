import pytest
from pythoncode.calculator import Calculator


@pytest.fixture(scope='module')
def get_calc():
    print('计算开始')
    calc = Calculator()
    yield calc
    print("计算结束")

# @pytest.fixture(scope="function",params=['tom','jerry'])
# def login():
#     #setup操作
#     print("登录操作")
#     #相当于return
#     yield ['tom',123456]
#     #teardown操作
#     print('登出操作')
#
# @pytest.fixture(scope='session',autouse='true')
# def conn_db():
#     print('完成数据库连接')
#     yield "database"
#     print('关闭数据库连接')
