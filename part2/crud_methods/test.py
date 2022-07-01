import sys
import unittest
import os
from pathlib import Path
from guides_sql import CREATE_TABLE, INSERT_VALUES
from sqlalchemy import text
import main
import solution

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import ResponseTestsMixin  # noqa: E402


class RoutesTestCase(SkyproTestCase, ResponseTestsMixin):

    @classmethod
    def setUpClass(cls):
        cls.instance_to_create = {
            "surname": "Иванов",
            "full_name": "Иван Иванов",
            "tours_count": 7,
            "bio": "Провожу экскурсии по крышам СПб",
            "is_pro": True,
            "company": "Удивительные экскурсии"
        }

    def setUp(self):
        main.db.metadata.drop_all()
        solution.db.metadata.drop_all()
        self.guide = main.Guide
        self.author_guide = solution.Guide

        with main.Session() as ses:
            ses.execute(text(CREATE_TABLE))
            ses.execute(text(INSERT_VALUES))
            ses.commit()

        with solution.Session() as ses:
            ses.execute(text(CREATE_TABLE))
            ses.execute(text(INSERT_VALUES))
            ses.commit()

    def test_get_all_method_works_correct(self):
        try:
            guides = self.guide.get_all()
        except Exception:
            self.fail("Проверьте, что метод Guide.get_all работает корректно")
        self.assertTrue(
            isinstance(guides, list),
            "Проверьте, что метод get_all возвращает список"
        )
        self.assertTrue(
            len(guides) == len(self.author_guide.get_all()),
            "Проверьте, что метод get_all возвращает все записи"
        )
        self.assertTrue(
            isinstance(guides[0], self.guide),
            "Проверьте, что метод get_all возвращает список, в котором содержатся экземпляры класса Guide"
        )

    def test_get_by_id_method_works_correct(self):
        guide_id = 3
        try:
            guide = self.guide.get(guide_id)
        except Exception:
            self.fail("Проверьте что метод Guide.get работает корректно")
        self.assertTrue(
            isinstance(guide, main.Guide),
            "Проверьте, что метод get возвращает объект Guide"
        )
        self.assertTrue(
            guide.id == guide_id,
            "Проверьте, что метод get возвращает объект с правильным id"
        )

    def test_delete_method_works_correct(self):
        guide_id = 4
        with main.Session() as ses:
            guides_count = ses.query(main.Guide).count()
        try:
            self.guide.delete(guide_id)
        except Exception:
            self.fail("Проверьте, что метод delete работает корректно")
        with main.Session() as ses:
            guides_count_after_delete = ses.query(main.Guide).count()
        self.assertTrue(
            guides_count == guides_count_after_delete + 1,
            "Проверьте, что метод delete удаляет объект из базы"
        )

    def test_create_method_works_correct(self):
        with main.Session() as ses:
            guides_count = ses.query(main.Guide).count()
        try:
            new_guide = self.guide.create(**self.instance_to_create)
        except Exception:
            self.fail("Проверьте, что метод Guide.create работает при передаче ей всех аргументов модели")
        with main.Session() as ses:
            guides_count_after_create = ses.query(main.Guide).count()
        self.assertTrue(
            guides_count == guides_count_after_create - 1,
            "Проверьте, что метод create создает объект из базы"
        )

    def test_filter_method_works_correct(self):
        expected_tours_count = 5
        try:
            filtered_guides = self.guide.filter_by_tours_count(expected_tours_count)
        except Exception:
            self.fail("Проверьте, что метод Guide.filter_by_tours_count работает корректно")
        self.assertTrue(
            isinstance(filtered_guides, list),
            "Проверьте, что метод filter_by_tours_count возвращает список объектов"
        )
        for guide in filtered_guides:
            self.assertTrue(
                guide.tours_count == expected_tours_count,
                "Проверьте, что метод filter_by_tours_count корректно фильтрует объекты"
            )


if __name__ == "__main__":
    unittest.main()
