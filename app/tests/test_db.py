# app/tests/test_db.py
from flask_testing import TestCase
from app.repository.db import app, db


class TestDB(TestCase):

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/AZAG_DB"
    TESTING = True

    def create_app(self):
        return app

    def test_connection(self):
        self.assertTrue(db.engine.connect())  # 测试连接是否成功

    def test_query_myTable(self):
        from app.models.mytable import MYTABLE  # 导入MyTable模型类，假设它定义在app/models.py文件中
        results = MYTABLE.query.all()  # 查询myTable数据表中的所有数据
        for row in results:
            print(row)  # 打印每一行数据
