import sys
import unittest
import os
from pathlib import Path

import main

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin  # noqa: E402


class ToursUpdaterTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_function_retuns_correct_value(self):
        guide_id = 3
        with main.Session() as ses:
            tours = ses.query(main.Guide).filter_by(id=guide_id).first().tours_count
        try:
            main.Guide.update_tours_counter(guide_id)
        except Exception:
            self.fail("Проверьте, что метод update_tours_count работает корректно")
        with main.Session() as ses:
            tours_after_update = ses.query(main.Guide).filter_by(id=guide_id).first().tours_count
            self.assertTrue(
                tours == tours_after_update - 1,
                "Проверьте, что после применения метода, число туров у гида с переданным ID увеличивается на 1"
            )


if __name__ == "__main__":
    unittest.main()
