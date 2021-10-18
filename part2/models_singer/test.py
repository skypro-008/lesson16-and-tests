import sys
import unittest
from pathlib import Path

import main
import solution
import sqlalchemy

BASENAME = 'lesson16-and-tests'
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin  # noqa: E402

MODEL_NAME = 'City'


class CityTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_model_columns_is_correct(self):
        student_columns = self.get_cursor_info(main.cursor).get('columns')
        author_columns = self.get_cursor_info(solution.cursor).get('columns')
        self.assertEqual(student_columns, author_columns,
                         (r'%@Проверьте, что правильно определили '
                          'поля модели. '
                          f'Вы выбрали {student_columns}, тогда '
                          f'как необходимо {author_columns}'))

    def test_model_fields_has_correct_types(self):
        model = main.City
        self.assertTrue(
            isinstance(model.id.type, sqlalchemy.Integer),
            f"%@Проверьте имеет ли поле 'id' модели {MODEL_NAME} "
            "тип Integer")

        self.assertTrue(
            isinstance(model.name.type, sqlalchemy.String),
            f"%@Проверьте имеет ли поле 'name' модели {MODEL_NAME} "
            "тип String")

        self.assertTrue(
            isinstance(model.country_ru.type, sqlalchemy.String),
            f"%@Проверьте имеет ли поле 'author' модели {MODEL_NAME} "
            "тип String")

        self.assertTrue(
            isinstance(model.population.type, sqlalchemy.Integer),
            f"%@Проверьте имеет ли поле 'year' модели {MODEL_NAME} "
            "тип Integer")


if __name__ == "__main__":
    unittest.main()
