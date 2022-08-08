import sys
import unittest
import os
from pathlib import Path
from sqlalchemy import text
import main
from guides_sql import add_tours, add_guides

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import ResponseTestsMixin  # noqa: E402


class LazyTestCase(SkyproTestCase, ResponseTestsMixin):

    def setUp(self):
        main.db.metadata.drop_all()
        main.db.metadata.create_all()
        add_guides(main.Session, main.Guide)
        add_tours(main.Session, main.Tour)

    def test_tours_by_guide(self):
        self.assertTrue(
            hasattr(main, "get_tours_by_guide"),
            "%@Проверьте, что функция get_tours_by_guide существует в модуле"
        )
        tours = main.get_tours_by_guide(1)
        self.assertTrue(
            isinstance(tours, list),
            "%@Проверьте, что функция get_tours_by_guide возвращает список"
        )
        self.assertTrue(
            isinstance(tours[0], main.Tour),
            "%@Проверьте что элемент списка возвращаемого функцией get_tours_by_guide является экземпляр класса Tour"
        )
        for tour in tours:
            self.assertTrue(
                tour.guide_id == 1,
                "%@Проверьте, что функция get_tours_by_guide возвращает туры только того гида, id которого передан в функцию"
                            )

    def test_get_guide_by_tour(self):
        self.assertTrue(
            hasattr(main, "get_guide_by_tour"),
            "%@Проверьте, что функция get_guide_by_tour существует в модуле"
        )
        guide = main.get_guide_by_tour(1)
        self.assertTrue(
            isinstance(guide, main.Guide),
            "%@Проверьте, что функция get_guide_by_tour возвращает объект Guide"
        )
        with main.Session() as session:
            tour = session.query(main.Tour).filter(main.Tour.id == 1).one()

        self.assertTrue(
            tour.guide_id == guide.id,
            "%@Проверьте, что функция get_guide_by_tour возвращает гида, который соответствует туру"
        )


if __name__ == "__main__":
    unittest.main()
