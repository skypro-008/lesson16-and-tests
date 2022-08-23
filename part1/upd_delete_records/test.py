import sys
import unittest
from pathlib import Path
import os

import main

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin  # noqa: E402


class CourseTestCase(SkyproTestCase, DataBaseTestsMixin):

    def setUp(self):
        self.session = main.Session
        self.user = main.User

    def test_delete_works_correct(self):
        with self.session() as session:
            before_delete = session.query(self.user).count()
        self.user.delete(1)
        with self.session() as session:
            after_delete = session.query(self.user).count()
        self.assertTrue(
            before_delete - 1 == after_delete,
            "%@Проверьте, что метод delete у Вашей модели удаляет объекты из базы")

    def test_update_works_correct(self):
        changes = dict(
            email="new@email.skypro.ru",
            password="new_password",
            full_name="new_full_name",
            price_per_hour=5000,
            city="NewCity",
        )
        for key, value in changes.items():
            self.user.update(2, **{key: value})
            with self.session() as session:
                new_user = session.query(self.user).get(2)
            self.assertTrue(
                getattr(new_user, key) == changes[key],
                f"%@Проверьте, что аттрибут {key} изменяется в базе данных"
            )



if __name__ == "__main__":
    unittest.main()
