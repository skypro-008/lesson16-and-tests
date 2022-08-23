import sys
import unittest
import os
from pathlib import Path
import main
from sqlalchemy.orm.relationships import RelationshipProperty

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import ResponseTestsMixin  # noqa: E402


class RelationshipTestCase(SkyproTestCase, ResponseTestsMixin):

    def setUp(self):
        main.db.metadata.drop_all()
        main.db.metadata.create_all()

    def test_guide_relationship(self):
        relationship_field = getattr(main.Guide, "tours", None)
        self.assertTrue(relationship_field, "%@Проверьте, что у класса Guide есть атрибут tours")
        self.assertTrue(
            isinstance(relationship_field.comparator, RelationshipProperty.Comparator),
            "Проверьте, что атрибут tours является связкой (relationship)"
        )
        self.assertTrue(
            str(relationship_field.expression) == 'guides.id = tours.guide_id',
            "%@Проверьте что аттрибут relationship класса Guide имеет правильные атрибуты"
        )

    def test_tour_relationship(self):
        relationship_field = getattr(main.Tour, "guide", None)
        self.assertTrue(relationship_field, "%@Проверьте, что у класса Tour есть атрибут guide")
        self.assertTrue(
            isinstance(relationship_field.comparator, RelationshipProperty.Comparator),
            "Проверьте, что атрибут guide является связкой (relationship)"
        )
        self.assertTrue(
            str(relationship_field.expression) == 'guides.id = tours.guide_id',
            "%@Проверьте что аттрибут relationship класса Guide имеет правильные атрибуты"
        )


if __name__ == "__main__":
    unittest.main()
