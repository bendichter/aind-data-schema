"""Script for defining UnitWithValue classes"""

from decimal import Decimal
from enum import Enum

from pydantic import create_model


class SizeUnit(Enum):
    """Enumeration of Length Measurements"""

    M = "meter"
    CM = "centimeter"
    MM = "millimeter"

    UM = "micrometer"
    NM = "nanometer"
    IN = "inch"
    PX = "pixel"


class MassUnit(Enum):
    """Enumeration of Mass Measurements"""

    KG = "kilogram"
    G = "gram"
    MG = "milligram"
    UG = "microgram"
    NG = "nanogram"


class FrequencyUnit(Enum):
    """Enumeration of Frequency Measurements"""

    KHZ = "kilohertz"
    HZ = "hertz"
    mHZ = "millihertz"


class VolumeUnit(Enum):
    """Enumeration of Volume Measurements"""

    L = "liter"
    ML = "milliliter"
    UL = "microliter"
    NL = "nanoliter"


class AngleUnit(Enum):
    """Enumeration of Angle Measurements"""

    RAD = "radians"
    DEG = "degrees"


class TimeUnit(Enum):
    """Enumeration of Time Measurements"""

    HR = "hour"
    M = "minute"
    S = "second"
    MS = "millisecond"
    US = "microsecond"
    NS = "nanosecond"


class PowerUnit(Enum):
    """Power units"""

    UW = "microwatt"
    MW = "milliwatt"


class CurrentUnit(Enum):
    """Current units"""

    UA = "microamps"


def create_unit_with_value(model_name, scalar_type, unit_type, unit_default):
    """this uses create_model instead of generics, which lets us set default values"""

    m = create_model(model_name, value=(scalar_type, ...), unit=(unit_type, unit_default))
    return m

coord_3d_fields = {'x': Decimal, 'y': Decimal, 'z': Decimal}
coord_2d_fields = {'x': Decimal, 'y': Decimal}

orientation_3d_fields = {'pitch': Decimal, 'yaw': Decimal, 'roll': Decimal}

module_orientation_3d_fields = {'arc_angle': Decimal, 'module_angle': Decimal, 'rotation_angle': Decimal}
module_orientation_2d_fields = {'arc_angle': Decimal, 'module_angle': Decimal}

size_3d_fields = {'length': Decimal, 'width': Decimal, 'height': Decimal}
size_2d_fields = {'width': Decimal, 'height': Decimal}

filter_size_fields = {'diameter': Decimal, 'width': Decimal, 'height': Decimal}

def create_unit_with_value(model_name, field_names_and_data_types, unit_type, unit_default, scalar_type = None):
    """this uses create_model instead of generics, which lets us set default values"""
    if scalar_type:
        m = create_model(model_name, **{k: (scalar_type, ...) for k in field_names_and_data_types}, unit=(unit_type, unit_default))
    else:
        m = create_model(model_name, **{k: (v, ...) for k, v in field_names_and_data_types.items()}, unit=(unit_type, unit_default))
    return m


Coord3DValue = create_unit_with_value("test_unit", {'x', 'y', 'z'}, SizeUnit, SizeUnit.MM, Decimal)

SizeValueMM = create_unit_with_value("SizeValueMM", Decimal, SizeUnit, SizeUnit.MM)
SizeValueCM = create_unit_with_value("SizeValueCM", Decimal, SizeUnit, SizeUnit.CM)
SizeValuePX = create_unit_with_value("SizeValuePX", int, SizeUnit, SizeUnit.PX)
SizeValueIN = create_unit_with_value("SizeValueIN", Decimal, SizeUnit, SizeUnit.IN)
SizeValueNM = create_unit_with_value("SizeValueNM", Decimal, SizeUnit, SizeUnit.NM)

FilterSizeValue = create_unit_with_value("FilterSizeValue", filter_size_fields, SizeUnit, SizeUnit.MM)

WaveLengthNM = create_unit_with_value("WaveLengthNM", int, SizeUnit, SizeUnit.NM)
MassValue = create_unit_with_value("MassValue", Decimal, MassUnit, MassUnit.MG)
VolumeValue = create_unit_with_value("VolumeValue", Decimal, VolumeUnit, VolumeUnit.NL)
FrequencyValueHZ = create_unit_with_value("FrequencyValue", Decimal, FrequencyUnit, FrequencyUnit.HZ)
AngleValue = create_unit_with_value("AngleValue", Decimal, AngleUnit, AngleUnit.DEG)
TimeValue = create_unit_with_value("TimeValue", Decimal, TimeUnit, TimeUnit.S)
PowerValue = create_unit_with_value("PowerValue", Decimal, PowerUnit, PowerUnit.MW)

CoordValue3D = create_unit_with_value("CoordValue3D", coord_3d_fields, SizeUnit, SizeUnit.MM)
CoordValue2D = create_unit_with_value("CoordValue2D", coord_2d_fields, SizeUnit, SizeUnit.MM)

SizeValue2DPX = create_unit_with_value("SizeValue2DPX", size_2d_fields, SizeUnit, SizeUnit.PX, int)
SizeValue3DMM = create_unit_with_value("SizeValue3DMM", size_3d_fields, SizeUnit, SizeUnit.MM)

OrientationValue3D = create_unit_with_value("OrientationValue3D", orientation_3d_fields, AngleUnit, AngleUnit.DEG)
ModuleOrientationValue2D = create_unit_with_value("ModuleOrientationValue2D", module_orientation_2d_fields, AngleUnit, AngleUnit.DEG)
ModuleOrientationValue3D = create_unit_with_value("ModuleOrientationValue3D", module_orientation_3d_fields, AngleUnit, AngleUnit.DEG)
