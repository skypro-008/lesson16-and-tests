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

MODEL_NAME = 'City'


class ToursCompanyNoneTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_function_returns_list(self):
        self.assertTrue(isinstance(main.Guide.get_freelancers(), list),
                        "%@Проверьте что метод get_freelancers"
                        " возвращает список значений")

        self.assertTrue(len(main.Guide.get_freelancers()) != 0,
                        "%@Проверьте что список значений возвращаемых "
                        " методом get_freelancers не пустой")

        self.assertTrue(
            isinstance(main.Guide.get_freelancers()[0], main.Guide),
            "%@Проверьте что список значений возвращаемых "
            " методом get_freelancers содержит экземпляры модели Guide")

    def test_function_retuns_correct_value(self):
        value_list = main.Guide.get_freelancers()
        for instance in value_list:
            self.assertEqual(
                instance.company, None,
                "%@Проверьте, что в результате, возвращаемом методом"
                " только те записи, в которых значение поля company=None")


if __name__ == "__main__":
    unittest.main()
