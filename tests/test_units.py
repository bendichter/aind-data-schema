"""Test utils.units"""

import unittest
from decimal import Decimal
from typing import TypeVar

from aind_data_schema.utils.units import SizeUnit, create_unit_with_value

ScalarType = TypeVar("ScalarType", Decimal, int)


class UnitsTests(unittest.TestCase):
    """Class for testing Utils.Units"""

    def test_units(self):
        """Tests creation of a SizeVal object"""

        self.assertIsNotNone(SizeUnit.MM)
        SizeValTest = create_unit_with_value("SizeValueMM", {'value'}, Decimal, SizeUnit, SizeUnit.MM)

        default = SizeValTest(value=10.1)

        self.assertEqual(default, SizeValTest(value=10.1, unit=SizeUnit.MM))

        ArbitraryValue = create_unit_with_value("ArbitraryValue", {'value'}, Decimal, SizeUnit, SizeUnit.IN)

        self.assertIsNotNone(ArbitraryValue(value=10, unit=SizeUnit.PX))


if __name__ == "__main__":
    unittest.main()
