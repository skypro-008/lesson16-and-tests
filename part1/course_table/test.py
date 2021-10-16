import sys
import unittest
from pathlib import Path

import flask_sqlalchemy

import main
import solution
import sqlalchemy
import inspect

BASENAME = 'lesson16-and-tests'
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin  # noqa: E402

MODEL_NAME = 'Course'


class CourseTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_module_bookschema_exists(self):
        self.assertTrue(
            hasattr(main, MODEL_NAME),
            f"%@Проверьте есть ли класс {MODEL_NAME} в модуле")

    def test_bookschema_is_class(self):
        self.assertTrue(
            inspect.isclass(main.Course),
            f"%@Проверьте, что {MODEL_NAME} это класс"
        )

    def test_bookschema_inheritance_is_correct(self):
        self.assertTrue(
            issubclass(main.Course, flask_sqlalchemy.Model),
            ("%@Проверьте, правильно ли указан родительский класс у "
             f"класса {MODEL_NAME}. Попробуйте использовать экземпляр "
             "класса SQLAlchemy")
        )

    def test_model_columns_is_correct(self):
        student_columns = self.get_cursor_info(main.cursor).get('columns')
        author_columns = self.get_cursor_info(solution.cursor).get('columns')
        self.assertEqual(student_columns, author_columns,
                         (r'%@Проверьте, что правильно определили '
                          'поля модели. '
                          f'Вы выбрали {student_columns}, тогда '
                          f'как необходимо {author_columns}'))

    def test_model_fields_has_correct_types(self):
        model = main.Course
        self.assertTrue(
            isinstance(model.id.type, sqlalchemy.Integer),
            f"%@Проверьте имеет ли поле 'id' модели {MODEL_NAME} "
            "тип Integer")

        self.assertTrue(
            isinstance(model.title.type, sqlalchemy.Text),
            f"%@Проверьте имеет ли поле 'title' модели {MODEL_NAME} "
            "тип Text")

        self.assertTrue(
            isinstance(model.subject.type, sqlalchemy.Text),
            f"%@Проверьте имеет ли поле 'subject' модели {MODEL_NAME} "
            "тип Text")

        self.assertTrue(
            isinstance(model.price.type, sqlalchemy.Integer),
            f"%@Проверьте имеет ли поле 'price' модели {MODEL_NAME} "
            "тип Integer")

        self.assertTrue(
            isinstance(model.weeks.type, sqlalchemy.Float),
            f"%@Проверьте имеет ли поле 'weeks' модели {MODEL_NAME} "
            "тип Float")


if __name__ == "__main__":
    unittest.main()
