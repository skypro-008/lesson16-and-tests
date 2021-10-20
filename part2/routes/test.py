import sys
import unittest
from pathlib import Path
from guides_sql import CREATE_TABLE, INSERT_VALUES
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
import json
import main
import solution

BASENAME = 'lesson16-and-tests'
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin  # noqa: E402


class CourseTestCase(SkyproTestCase, DataBaseTestsMixin):

    @classmethod
    def setUpClass(cls):
        cls.one_field_update = {
            "surname": "Федоров"
        }
        cls.three_fields_update = {
            "surname": "Петров",
            "full_name": "Петр Петров",
            "tours_count": 500,
        }

    def setUp(self):
        self.app = main.app.test_client()
        self.db = main.db
        self.db.drop_all()
        with self.db.session.begin():
            self.db.session.execute(text(CREATE_TABLE))
            self.db.session.execute(text(INSERT_VALUES))
        self.author_app = solution.app.test_client()
        self.author_db = solution.db
        self.author_db.drop_all()
        with self.db.session.begin():
            self.author_db.session.execute(text(CREATE_TABLE))
            self.author_db.session.execute(text(INSERT_VALUES))

    def test_get_method_is_available_and_works_correct(self):
        url = '/guides'
        response = self.app.get(url)
        self.assertEqual(
            response.status_code, 200,
            (f"%@Проверьте, что GET-запрос на адрес {url} возвращает"
             "код 200"))
        data = json.loads(response.data)
        self.assertTrue(
            isinstance(data, list),
            f"%@Проверьте что в ответ на GET-запрос по адресу {url}"
            "возвращается список"
        )
        self.assertEqual(
            len(data), 10,
            f"%@Проверьте, что в ответ на GET-запрос по адресу {url} "
            "возвращаются все объекты"
        )
        author_response = self.author_app.get(url)
        author_data = json.loads(author_response.data)[0]
        student_items = data[0].items()
        for key, value in student_items:
            self.assertIn(
                key,
                author_data.keys(),
                f"%@ Проверьте, что ответ на GET-запрос по адресу {url} "
                f"содержит поле {key}")
            self.assertEqual(
                value,
                author_data[key],
                f"%@ Проверьте, что ответ на GET-запрос по адресу {url} "
                f"в поле {key} содержится правильное значение")

    def test_get_filter_method_is_available_and_works_correct(self):
        tours_count = 1
        filter_value = 'tours_count'
        url = f'/guides?{filter_value}={tours_count}'
        response = self.app.get(url)
        self.assertEqual(
            response.status_code, 200,
            (f"%@Проверьте, что GET-запрос на адрес {url} возвращает "
             "код 200"))
        data = json.loads(response.data)
        self.assertTrue(
            isinstance(data, list),
            f"%@Проверьте что в ответ на GET-запрос по адресу {url}"
            "возвращается список"
        )
        author_response = self.author_app.get(url)
        author_data = json.loads(author_response.data)[0]
        student_items = data[0].items()
        for instance in data:
            self.assertEqual(
                instance[filter_value], tours_count,
                f"%@Проверьте что ответ на GET-запрос по адресу {url} "
                "содержит правильные данные")
        for key, value in student_items:
            self.assertIn(
                key,
                author_data.keys(),
                f"%@ Проверьте, что ответ на GET-запрос по адресу {url} "
                f"содержит поле {key}")
            self.assertEqual(
                value,
                author_data[key],
                f"%@ Проверьте, что ответ на GET-запрос по адресу {url} "
                f"в поле {key} содержится правильное значение")

    def test_get_id_method_is_available_and_works_correct(self):
        url = '/guides/1'
        response = self.app.get(url)
        self.assertEqual(
            response.status_code, 200,
            (f"%@Проверьте, что GET-запрос на адрес {url} возвращает"
             "код 200"))
        data = json.loads(response.data)
        self.assertTrue(
            isinstance(data, dict),
            f"%@Проверьте что в ответ на GET-запрос по адресу {url}"
            "возвращается словарь"
        )
        author_response = self.author_app.get(url)
        author_data = json.loads(author_response.data)
        student_items = data.items()
        for key, value in student_items:
            self.assertIn(
                key,
                author_data.keys(),
                f"%@ Проверьте, что ответ на GET-запрос по адресу {url} "
                f"содержит поле {key}")
            self.assertEqual(
                value,
                author_data[key],
                f"%@ Проверьте, что ответ на GET-запрос по адресу {url} "
                f"в поле {key} содержится правильное значение")

    def test_put_method_is_available_and_works_correct(self):
        url = '/guides/1'
        response = self.app.put(url, data=json.dumps(self.one_field_update))
        self.assertIn(
            response.status_code, [200, 204],
            ("%@Проверьте, что PUT-запрос с одним полем на адрес"
             f" {url} возвращает код 200 или 204"))
        result = self.db.session.execute(
            text('select `surname` from guide where id=1')).fetchall()
        self.one_field_update.get('surname')
        self.assertEqual(
            result[0][0], self.one_field_update.get('surname'),
            ("%@Проверьте, что при выполнении PUT-запроса с изменением одного "
             " поля происходят соответствующие изменения в БД"))
        self.app.put(url, data=json.dumps(self.three_fields_update))
        result = self.db.session.execute(
            text('select `surname`, `full_name`, `tours_count` from guide where id=1')).fetchall()
        for value in self.three_fields_update.values():
            self.assertIn(
                value, result[0],
                ("%@Проверьте, что при выполнении PUT-запроса с"
                 " изменением нескольких полей происходят"
                 " соответствующие изменения в БД"))
        self.assertIn(
            response.status_code, [200, 204],
            ("%@Проверьте, что PUT-запрос с несколькими полями на адрес"
             f" {url} возвращает код 200 или 204"))

    def test_delete_method_is_available_and_works_correct(self):
        url = '/guides/1'
        response = self.app.post(url)
        self.assertEqual(
            response.status_code, 204,
            (f"%@Проверьте, что POST-запрос на адрес"
             f" {url} возвращает код 200 или 204"))
        result = self.db.session.execute(
            text('select * from guide where id=1')).fetchall()
        self.assertTrue(
            result == [],
            f"%@Проверьте что POST-запрос на адрес {url} "
            " удаляет запись из базы данных"
        )

    def tearDown(self):
        self.db.session.close()
        self.author_db.session.close()


if __name__ == "__main__":
    unittest.main()
