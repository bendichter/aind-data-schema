""" ephys rig schemas """

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import Field

from ..base import AindCoreModel, AindModel
from ..device import DAQ, Device, DeviceBase


class Size2d(AindModel):
    """2D size of an object"""

    width: int = Field(..., title="Width")
    height: int = Field(..., title="Height")
    unit: str = Field("pixels", title="Size units")


class Orientation3d(AindModel):
    """3D orientation of an object"""

    pitch: float = Field(..., title="Angle pitch", ge=0, le=360)
    yaw: float = Field(..., title="Angle yaw", ge=0, le=360)
    roll: float = Field(..., title="Angle roll", ge=0, le=360)
    unit: str = Field("degrees", title="Angle units")


class ModuleOrientation2d(AindModel):
    """2D module orientation of an object"""

    arc_angle: float = Field(..., title="Arc Angle")
    module_angle: float = Field(..., title="Module Angle")
    unit: str = Field("degrees", title="Degrees")


class ModuleOrientation3d(ModuleOrientation2d):
    """3D module orientation of an object"""

    rotation_angle: float = Field(..., title="Rotation angle")


class Position3d(AindModel):
    """Position of a 3d object"""

    x: float = Field(..., title="Position X")
    y: float = Field(..., title="Position Y")
    z: float = Field(..., title="Position Z")
    unit: str = Field("None", title="Position units")


class HarpDeviceName(Enum):
    """Harp device name"""

    BEHAVIOR = "Behavior"
    CAMERA_CONTROLLER = "Camera Controller"
    LOAD_CELLS = "Load Cells"
    SOUND_BOARD = "Sound Board"
    TIMESTAMP_GENERATOR = "Timestamp Generator"
    INPUT_EXPANDER = "Input Expander"


class HarpDevice(Device):
    """Describes a Harp device"""

    name: HarpDeviceName = Field(..., title="Name")
    device_version: str = Field(..., title="Device version")


class CameraName(Enum):
    """Camera name"""

    BODY_CAMERA = "Body Camera"
    EYE_CAMERA = "Eye Camera"
    FACE_CAMERA = "Face Camera"


class Camera(Device):
    """Description of camera"""

    name: CameraName = Field(..., title="Name")
    orientation: Orientation3d = Field(..., title="Camera orientation")
    position: Position3d = Field(..., title="Camera position")
    recording_software: Optional[str] = Field(None, title="Recording software")
    recording_software_version: Optional[str] = Field(
        None, title="Recording software version"
    )


class MousePlatform(Device):
    """Description of a mouse platform"""

    surface_material: Optional[str] = Field(None, title="Surface material")


class Disc(MousePlatform):
    """Description of a running disc"""

    platform_type: str = Field("Disc", title="Platform type", const=True)
    radius: float = Field(..., title="Radius (cm)", units="cm", ge=0)
    date_surface_replaced: Optional[datetime] = Field(
        None, title="Date surface replaced"
    )


class Tube(MousePlatform):
    """Description of a tube platform"""

    platform_type: str = Field("Tube", title="Platform type", const=True)
    diameter: float = Field(..., title="Diameter (cm)", units="cm", ge=0)


class Treadmill(MousePlatform):
    """Descrsiption of treadmill platform"""

    platform_type: str = Field("Treadmill", title="Platform type", const=True)


class StickMicroscope(Device):
    """Description of a stick microscope used to monitor probes during insertion"""

    orientation: ModuleOrientation2d = Field(
        ..., title="Microscope orientation"
    )


class Manipulator(DeviceBase):
    """Description of manipulator"""

    orientation: ModuleOrientation3d = Field(
        ..., title="Manipulator orientation"
    )


class LaserName(Enum):
    """Laser name"""

    LASER_A = "Laser A"
    LASER_B = "Laser B"
    LASER_C = "Laser C"
    LASER_D = "Laser D"


class Laser(Device):
    """Description of a laser used in ephys recordings"""

    name: LaserName = Field(..., title="Laser Name")

    wavelength: Optional[int] = Field(
        None, title="Wavelength (nm)", units="nm", ge=300, le=1000
    )
    maximum_power: Optional[float] = Field(
        None, title="Maximum power (mW)", units="mW"
    )
    coupling_efficiency: Optional[float] = Field(
        None,
        title="Coupling efficiency (percent)",
        units="percent",
        ge=0,
        le=100,
    )
    calibration_data: Optional[str] = Field(
        None, description="path to calibration data", title="Calibration data"
    )
    calibration_date: Optional[datetime] = Field(
        None, title="Calibration date"
    )
    laser_manipulator: Manipulator = Field(..., title="Manipulator")


class LaserModule(DeviceBase):
    """Description of a laser housing module used in ephys recordings"""

    lasers: List[Laser] = Field(..., title="Lasers")


class Monitor(Device):
    """Description of a visual monitor"""

    refresh_rate: int = Field(
        ..., title="Refresh rate (Hz)", units="Hz", ge=60
    )
    size: Size2d = Field(..., title="Monitor size")
    position: Position3d = Field(..., title="Monitor position")
    orientation: Orientation3d = Field(..., title="Monitor orientation")
    viewing_distance: float = Field(
        ..., title="Viewing distance (cm)", units="cm"
    )
    contrast: int = Field(
        ...,
        description="Monitor's contrast setting",
        title="Contrast (percent)",
        units="percent",
        ge=0,
        le=100,
    )
    brightness: int = Field(
        ...,
        description="Monitor's brightness setting",
        title="Brightness",
        ge=0,
        le=100,
    )


class ProbeName(Enum):
    """Probe name"""

    PROBE_A = "Probe A"
    PROBE_B = "Probe B"
    PROBE_C = "Probe C"
    PROBE_D = "Probe D"
    PROBE_E = "Probe E"
    PROBE_F = "Probe F"
    PROBE_G = "Probe G"
    PROBE_H = "Probe H"
    PROBE_I = "Probe I"
    PROBE_J = "Probe J"


class ProbeModel(Enum):
    """Probe model name"""

    NP1 = "Neuropixels 1.0"
    NP_UHD_FIXED = "Neuropixels UHD (Fixed)"
    NP_UHD_SWITCHABLE = "Neuropixels UHD (Switchable)"
    NP2_SINGLE_SHANK = "Neuropixels 2.0 (Single Shank)"
    NP2_MULTI_SHANK = "Neuropixels 2.0 (Multi Shank)"
    NP2_QUAD_BASE = "Neuropixels 2.0 (Quad Base)"
    NP_OPTO_DEMONSTRATOR = "Neuropixels Opto (Demonstrator)"
    MI_ULED_PROBE = "Michigan uLED Probe (Version 1)"
    MP_PHOTONIC_V1 = "MPI Photonic Probe (Version 1)"


class EphysProbe(Device):
    """Description of an ephys probe"""

    name: ProbeName = Field(..., title="Name")
    probe_manipulator: Manipulator = Field(..., title="Manipulator")
    calibration_data: Optional[str] = Field(
        ..., title="Calibration data", description="Path to calibration data"
    )
    calibration_date: Optional[datetime] = Field(
        None, title="Calibration date"
    )


class EphysRig(AindCoreModel):
    """Description of an ephys rig"""

    describedBy: str = Field(
        "https://github.com/AllenNeuralDynamics/data_schema/blob/main/schemas/ephys/ephys_rig.py",
        description="The URL reference to the schema.",
        title="Described by",
        const=True,
    )
    schema_version: str = Field(
        "0.5.0", description="schema version", title="Version", const=True
    )
    rig_id: str = Field(
        ..., description="room_stim apparatus_version", title="Rig ID"
    )
    probes: Optional[List[EphysProbe]] = Field(
        None, title="Ephys probes", unique_items=True
    )
    cameras: Optional[List[Camera]] = Field(
        None, title="Cameras", unique_items=True
    )
    laser_modules: Optional[List[LaserModule]] = Field(
        None, title="Lasers", unique_items=True
    )
    visual_monitors: Optional[List[Monitor]] = Field(
        None, title="Visual monitor", unique_items=True
    )
    mouse_platform: Optional[Union[Tube, Treadmill, Disc]] = Field(
        None, title="Mouse platform"
    )
    harp_devices: Optional[List[HarpDevice]] = Field(
        None, title="Harp devices"
    )
    stick_microscopes: Optional[List[StickMicroscope]] = Field(
        None, title="Stick microscopes"
    )
    daqs: Optional[List[DAQ]] = Field(None, title="DAQ devices")
