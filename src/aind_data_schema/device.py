""" schema for various Devices """

from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from aind_data_schema.base import AindModel, BaseNameEnumMeta, EnumSubset, PIDName, Registry
from aind_data_schema.utils.units import create_unit_with_value, SizeUnit, MassUnit, FrequencyUnit, VolumeUnit, TimeUnit, AngleUnit, PowerUnit, CurrentUnit


class DeviceDriver(Enum):
    """DeviceDriver name"""

    OPENGL = "OpenGL"
    VIMBA = "Vimba"
    NVIDIA = "Nvidia Graphics"


class Manufacturer(Enum, metaclass=BaseNameEnumMeta):
    """Device manufacturer name"""

    ALLIED = PIDName(name="Allied")
    ASI = PIDName(
        name="Applied Scientific Instrumentation",
        abbreviation="ASI",
    )
    BASLER = PIDName(name="Basler")
    CAMBRIDGE_TECHNOLOGY = PIDName(name="Cambridge Technology")
    CHROMA = PIDName(name="Chroma")
    COHERENT_SCIENTIFIC = PIDName(
        name="Coherent Scientific",
        registry=Registry.ROR,
        registry_identifier="031tysd23",
    )
    COMPUTAR = PIDName(name="Computar")
    CUSTOM = PIDName(name="Custom")
    DORIC = PIDName(
        name="Doric",
        registry=Registry.ROR,
        registry_identifier="059n53q30",
    )
    EALING = PIDName(name="Ealing")
    EDMUND_OPTICS = PIDName(
        name="Edmund Optics",
        registry=Registry.ROR,
        registry_identifier="01j1gwp17",
    )
    AILIPU = PIDName(name="Ailipu Technology Co")
    FLIR = PIDName(
        name="Teledyne FLIR",
        abbreviation="FLIR",
        registry=Registry.ROR,
        registry_identifier="01j1gwp17",
    )
    HAMAMATSU = PIDName(
        name="Hamamatsu",
        registry=Registry.ROR,
        registry_identifier="03natb733",
    )
    IMAGING_SOURCE = PIDName(name="The Imaging Source")
    IMEC = PIDName(
        name="Interuniversity Microelectronics Center",
        abbreviation="IMEC",
        registry=Registry.ROR,
        registry_identifier="02kcbn207",
    )
    JULABO = PIDName(name="Julabo")
    LEICA = PIDName(name="Leica")
    LG = PIDName(
        name="LG",
        registry=Registry.ROR,
        registry_identifier="02b948n83",
    )
    LIFECANVAS = PIDName(name="LifeCanvas")
    MIGHTY_ZAP = PIDName(name="IR Robot Co")
    MKS_NEWPORT = PIDName(
        name="MKS Newport",
        registry=Registry.ROR,
        registry_identifier="00k17f049",
    )
    MPI = PIDName(name="MPI", abbreviation="MPI")
    NATIONAL_INSTRUMENTS = PIDName(
        name="National Instruments",
        registry=Registry.ROR,
        registry_identifier="026exqw73",
    )
    NEW_SCALE_TECHNOLOGIES = PIDName(name="New Scale Technologies")
    NIKON = PIDName(
        name="Nikon",
        registry=Registry.ROR,
        registry_identifier="0280y9h11",
    )
    OEPS = PIDName(
        name="Open Ephys Production Site",
        abbreviation="OEPS",
        registry=Registry.ROR,
        registry_identifier="007rkz355",
    )
    OLYMPUS = PIDName(
        name="Olympus",
        registry=Registry.ROR,
        registry_identifier="02vcdte90",
    )
    OPTOTUNE = PIDName(name="Optotune")
    OXXIUS = PIDName(name="Oxxius")
    PRIZMATIX = PIDName(name="Prizmatix")
    QUANTIFI = PIDName(name="Quantifi")
    SEMROCK = PIDName(name="Semrock")
    THORLABS = PIDName(
        name="Thorlabs",
        registry=Registry.ROR,
        registry_identifier="04gsnvb07",
    )
    TMC = PIDName(name="Technical Manufacturing Corporation", abbreviation="TMC")
    VIEWORKS = PIDName(name="Vieworks")
    VORTRAN = PIDName(name="Vortran")
    OTHER = PIDName(name="Other")


class Coupling(Enum):
    """Laser coupling type"""

    FREE_SPACE = "Free-space"
    MMF = "Multi-mode fiber"
    SMF = "Single-mode fiber"
    OTHER = "Other"


class DataInterface(Enum):
    """Connection between a device and a PC"""

    CAMERALINK = "CameraLink"
    COAX = "Coax"
    ETH = "Ethernet"
    PCIE = "PCIe"
    PXI = "PXI"
    USB = "USB"
    OTHER = "Other"


class FilterType(Enum):
    """Filter type"""

    BANDPASS = "Band pass"
    DICHROIC = "Dichroic"
    LONGPASS = "Long pass"
    MULTIBAND = "Multiband"
    ND = "Neutral density"
    NOTCH = "Notch"
    SHORTPASS = "Short pass"


class LensSize(Enum):
    """Lens size value"""

    LENS_SIZE_1 = 1
    LENS_SIZE_2 = 2


class CameraChroma(Enum):
    """Color vs. black & white"""

    COLOR = "Color"
    BW = "Monochrome"


class DaqChannelType(Enum):
    """DAQ Channel type"""

    AI = "Analog Input"
    AO = "Analog Output"
    DI = "Digital Input"
    DO = "Digital Output"


class RelativePosition(AindModel):
    """Set of 6 values describing relative position on a rig"""

    relative_position: Optional[create_unit_with_value("relative_position", {'pitch', 'yaw', 'roll'}, Decimal, AngleUnit, AngleUnit.DEG)] = Field(None, title="Geometric coordinates (x,y,z)")

    coordinate_system: Optional[str] = Field(None, title="Description of the coordinate system used")


class Size2d(AindModel):
    """2D size of an object"""
    Size2D: create_unit_with_value("Size2D", {'width','height'}, int, SizeUnit, SizeUnit.PX) = Field(..., title="2D size (PX)")

class Orientation3d(AindModel): # TODO: This can become a subunit of RelativePosition
    """3D orientation of an object"""

    Orientation3D: create_unit_with_value("Orientation3D", {'pitch', 'yaw', 'roll'}, Decimal, AngleUnit, AngleUnit.DEG) = Field(..., title="Orientation (pitch, yaw, roll)")


class ModuleOrientation2d(AindModel):
    """2D module orientation of an object"""

    ModuleOrientation2D: create_unit_with_value("ModuleOrientation2D", {'arc_angle', 'module_angle'}, Decimal, AngleUnit, AngleUnit.DEG) = Field(..., title="Orientation (arc_angle, module_angle)")


class ModuleOrientation3d(AindModel):
    """3D module orientation of an object"""

    ModuleOrientation3D: create_unit_with_value("ModuleOrientation3D", {'arc_angle', 'module_angle', 'rotation_angle'}, Decimal, AngleUnit, AngleUnit.DEG) = Field(..., title="Orientation (arc_angle, module_angle, rotation_angle)")



class Coordinates3d(AindModel): # TODO: This can also become a subunit of RelativePosition
    """Coordinates in a 3D grid"""

    coordinates_3D: create_unit_with_value("Coordinates3D", {'x','y','z'}, Decimal, SizeUnit, SizeUnit.MM) = Field(..., title="3D Coordinate Position (x, y, z)")


class Device(AindModel):
    """Generic device"""

    name: Optional[str] = Field(None, title="Device name")
    serial_number: Optional[str] = Field(None, title="Serial number")
    manufacturer: Optional[Manufacturer] = Field(None, title="Manufacturer")
    model: Optional[str] = Field(None, title="Model")
    notes: Optional[str] = Field(None, title="Notes")


class Software(AindModel):
    """Description of generic software"""

    name: str = Field(..., title="Software name")
    version: str = Field(..., title="Software version")
    parameters: Optional[dict] = Field(None, title="Software parameters", additionalProperties={"type": "string"})


class MotorizedStage(Device):
    """Description of motorized stage"""

    travel: create_unit_with_value("Travel", {'value'}, Decimal, SizeUnit, SizeUnit.MM) = Field(..., title="Travel of device (mm)", units="mm")

    # optional fields
    firmware: Optional[str] = Field(None, title="Firmware")


class Camera(Device):
    """Device that acquires images and streams them to a computer"""

    # required fields
    data_interface: DataInterface = Field(..., title="Type of connection to PC")
    manufacturer: EnumSubset[
        Manufacturer.AILIPU,
        Manufacturer.ALLIED,
        Manufacturer.BASLER,
        Manufacturer.EDMUND_OPTICS,
        Manufacturer.FLIR,
        Manufacturer.IMAGING_SOURCE,
        Manufacturer.THORLABS,
        Manufacturer.OTHER,
    ]
    computer_name: str = Field(..., title="Name of computer receiving data from this camera")
    max_frame_rate: create_unit_with_value("Max Framerate", {'Frequency'}, Decimal, FrequencyUnit, FrequencyUnit.HZ) = Field(..., title="Maximum frame rate (Hz)", units="Hz")
    pixel_width: create_unit_with_value("Pixel Width", {'pixels'}, int, SizeUnit, SizeUnit.PX) = Field(..., title="Width of the sensor in pixels")
    pixel_height: create_unit_with_value("Pixel Height", {'pixels'}, int, SizeUnit, SizeUnit.PX) = Field(..., title="Height of the sensor in pixels")
    chroma: CameraChroma = Field(..., title="Color or Monochrome")

    # optional fields
    sensor_format: Optional[str] = Field(None, title="Size of the sensor") #TODO: What unit???
    format_unit: Optional[str] = Field(None, title="Format unit")
    recording_software: Optional[Software] = Field(None, title="Recording software")
    driver: Optional[DeviceDriver] = Field(None, title="Driver")
    driver_version: Optional[str] = Field(None, title="Driver version")


class Lens(Device):
    """Lens used to focus light onto a camera sensor"""

    # required fields
    manufacturer: EnumSubset[
        Manufacturer.COMPUTAR, Manufacturer.EDMUND_OPTICS, Manufacturer.THORLABS, Manufacturer.OTHER
    ]

    # optional fields
    focal_length: Optional[create_unit_with_value("Focal length", {'value'}, Decimal, SizeUnit, SizeUnit.MM)] = Field(None, title="Focal length of the lens", units="mm")
    size: Optional[create_unit_with_value("Lens Size", {'size'}, LensSize, SizeUnit, SizeUnit.IN)] = Field(None, title="Size (inches)") #TODO: Make sure this works with LensSize type
    optimized_wavelength_range: Optional[create_unit_with_value("Optimized Wavelength Range", {'value'}, Decimal, SizeUnit, SizeUnit.NM)] = Field(None, title="Optimized wavelength range (nm)") # TODO: Covert this to lower/upper bound?
    max_aperture: Optional[str] = Field(None, title="Max aperture (e.g. f/2)")


class Filter(Device):
    """Filter used in a light path"""

    # required fields
    filter_type: FilterType = Field(..., title="Type of filter")
    manufacturer: EnumSubset[
        Manufacturer.EDMUND_OPTICS,
        Manufacturer.CHROMA,
        Manufacturer.SEMROCK,
        Manufacturer.THORLABS,
        Manufacturer.OTHER,
    ]

    # optional fields # TODO: Get input on how to split this data up
    filter_size: Optional[create_unit_with_value("Filter Size", {'width', 'height'}, Decimal, SizeUnit, SizeUnit.MM)] = Field(None, title="Filter Size (width, height)")
    filter_diameter: Optional[create_unit_with_value("Filter Diameter", {'value'}, Decimal, SizeUnit, SizeUnit.MM)] = Field(None, title="Filter Size (diameter, width, height)")

    thickness: Optional[create_unit_with_value("Thickness", {'value'}, Decimal, SizeUnit, SizeUnit.MM)] = Field(None, title="Thickness (mm)")
    filter_wheel_index: Optional[int] = Field(None, title="Filter wheel index")
    cut_off_wavelength: Optional[create_unit_with_value("Cut-Off Wavelength", {'value'}, Decimal, SizeUnit, SizeUnit.NM)] = Field(None, title="Cut-off wavelength (nm)")
    cut_on_wavelength: Optional[create_unit_with_value("Cut-On Wavelength", {'value'}, Decimal, SizeUnit, SizeUnit.NM)] = Field(None, title="Cut-on wavelength (nm)")
    center_wavelength: Optional[create_unit_with_value("Center Wavelength", {'value'}, Decimal, SizeUnit, SizeUnit.NM)] = Field(None, title="Center wavelength (nm)")
    description: Optional[str] = Field(
        None, title="Description", description="More details about filter properties and where/how it is being used"
    )


class Immersion(Enum):
    """Immersion media name"""

    AIR = "air"
    MULTI = "multi"
    OIL = "oil"
    WATER = "water"
    OTHER = "other"


class Objective(Device):
    """Description of an objective device"""

    numerical_aperture: Decimal = Field(..., title="Numerical aperture (in air)")
    magnification: Decimal = Field(..., title="Magnification")
    immersion: Immersion = Field(..., title="Immersion")


class CameraTarget(Enum):
    """Target of camera"""

    BODY = "Body"
    BOTTOM = "Bottom"
    EYE = "Eye"
    FACE_BOTTOM = "Face bottom"
    FACE_SIDE = "Face side"
    SIDE = "Side"
    TONGUE = "Tongue"
    OTHER = "Other"


class CameraAssembly(AindModel):
    """Named assembly of a camera and lens (and optionally a filter)"""

    # required fields
    camera_assembly_name: str = Field(..., title="Camera assembly name")
    camera_target: CameraTarget = Field(..., title="Camera target")
    camera: Camera = Field(..., title="Camera")
    lens: Lens = Field(..., title="Lens")

    # optional fields
    filter: Optional[Filter] = Field(None, title="Filter")
    position: Optional[RelativePosition] = Field(None, title="Relative position of this assembly")


class DAQChannel(AindModel):
    """Named input or output channel on a DAQ device"""

    # required fields
    channel_name: str = Field(..., title="DAQ channel name")
    device_name: str = Field(..., title="Name of connected device")
    channel_type: DaqChannelType = Field(..., title="DAQ channel type")

    # optional fields
    port: Optional[int] = Field(None, title="DAQ port")
    channel_index: Optional[int] = Field(None, title="DAQ channel index")
    sample_rate: Optional[create_unit_with_value("Sample Rate", {'value'}, Decimal, FrequencyUnit, FrequencyUnit.HZ)] = Field(None, title="DAQ channel sample rate (Hz)", units="Hz")
    event_based_sampling: Optional[bool] = Field(
        False, title="Set to true if DAQ channel is sampled at irregular intervals"
    )


class DAQDevice(Device):
    """Data acquisition device containing multiple I/O channels"""

    # required fields
    data_interface: DataInterface = Field(..., title="Type of connection to PC")
    manufacturer: EnumSubset[
        Manufacturer.NATIONAL_INSTRUMENTS,
        Manufacturer.IMEC,
        Manufacturer.OEPS,
        Manufacturer.OTHER,
    ]
    computer_name: str = Field(..., title="Name of computer controlling this DAQ")

    # optional fields
    channels: Optional[List[DAQChannel]] = Field(None, title="DAQ channels")


class HarpDeviceType(Enum):
    """Harp device type"""

    BEHAVIOR = "Behavior"
    CAMERA_CONTROLLER = "Camera Controller"
    LOAD_CELLS = "Load Cells"
    SOUND_BOARD = "Sound Board"
    TIMESTAMP_GENERATOR = "Timestamp Generator"
    INPUT_EXPANDER = "Input Expander"


class HarpDevice(DAQDevice):
    """DAQ that uses the Harp protocol for synchronization and data transmission"""

    # required fields
    harp_device_type: HarpDeviceType = Field(..., title="Type of Harp device")
    harp_device_version: str = Field(..., title="Device version")

    # fixed values
    manufacturer: Manufacturer = Manufacturer.OEPS
    data_interface: DataInterface = Field("USB", const=True)


class Laser(Device):
    """Laser module with a specific wavelength (may be a sub-component of a larger assembly)"""

    # required fields
    lightsource_type: str = Field("Laser", title="Lightsource type")
    manufacturer: EnumSubset[
        Manufacturer.COHERENT_SCIENTIFIC,
        Manufacturer.HAMAMATSU,
        Manufacturer.OXXIUS,
        Manufacturer.QUANTIFI,
        Manufacturer.OTHER,
    ]
    wavelength: create_unit_with_value("WaveLength", {'value'}, int, SizeUnit, SizeUnit.NM) = Field(..., title="Wavelength (nm)")

    # optional fields
    maximum_power: Optional[create_unit_with_value("Maximum Power", {'value'}, int, SizeUnit, SizeUnit.NM)] = Field(None, title="Maximum power (mW)")
    coupling: Optional[Coupling] = Field(None, title="Coupling")
    coupling_efficiency: Optional[Decimal] = Field(
        None,
        title="Coupling efficiency (percent)",
        units="percent",
        ge=0,
        le=100,
    )
    coupling_efficiency_unit: Optional[str] = Field("percent", title="Coupling efficiency unit")
    item_number: Optional[str] = Field(None, title="Item number")
    calibration_data: Optional[str] = Field(None, description="Path to calibration data", title="Calibration data")
    calibration_date: Optional[datetime] = Field(None, title="Calibration date")


class LightEmittingDiode(Device):
    """Description of a Light Emitting Diode (LED) device"""

    lightsource_type: str = Field("LED", title="Lightsource type")
    manufacturer: EnumSubset[
        Manufacturer.DORIC,
        Manufacturer.PRIZMATIX,
        Manufacturer.THORLABS,
        Manufacturer.OTHER,
    ]
    wavelength: create_unit_with_value("WaveLength", {'value'}, int, SizeUnit, SizeUnit.NM) = Field(..., title="Wavelength (nm)")


class MousePlatform(Device):
    """Description of a mouse platform"""

    surface_material: Optional[str] = Field(None, title="Surface material")
    date_surface_replaced: Optional[datetime] = Field(None, title="Date surface replaced")


class Disc(MousePlatform):
    """Description of a running disc"""

    platform_type: str = Field("Disc", title="Platform type", const=True)
    radius: create_unit_with_value("Radius", {'value'}, Decimal, SizeUnit, SizeUnit.CM) = Field(..., title="Radius (cm)", units="cm", ge=0)
    output: Optional[DaqChannelType] = Field(None, description="analog or digital electronics")
    encoder: Optional[str] = Field(None, title="Encoder", description="Encoder hardware type")
    decoder: Optional[str] = Field(None, title="Decoder", description="Decoder chip type")
    encoder_firmware: Optional[Software] = Field(
        None, title="Encoder firmware", description="Firmware to read from decoder chip counts"
    )


class Tube(MousePlatform):
    """Description of a tube platform"""

    platform_type: str = Field("Tube", title="Platform type", const=True)
    diameter: create_unit_with_value("Diameter", {'value'}, Decimal, SizeUnit, SizeUnit.CM) = Field(..., title="Diameter")


class Treadmill(MousePlatform):
    """Description of treadmill platform"""

    platform_type: str = Field("Treadmill", title="Platform type", const=True)
    treadmill_width: create_unit_with_value("Treadmill Width", {'value'}, Decimal, SizeUnit, SizeUnit.CM) = Field(..., title="Width of treadmill (mm)", units="mm")


class Monitor(Device):
    """Visual display"""

    # required fields
    manufacturer: EnumSubset[Manufacturer.LG]
    refresh_rate: create_unit_with_value("Refresh Rate", {'value'}, Decimal, FrequencyUnit, FrequencyUnit.HZ) = Field(..., title="Refresh rate (Hz)", units="Hz", ge=60)
    size2D: create_unit_with_value("Size2D", {'width', 'height'}, SizeUnit, SizeUnit.PX) = Field(..., title="Size (width, heigh) in pixels", units="pixels")
    viewing_distance: create_unit_with_value("Viewing Distance", {'value'}, Decimal, SizeUnit, SizeUnit.CM) = Field(..., title="Viewing distance (cm)", units="cm")

    # optional fields
    contrast: Optional[int] = Field(
        ...,
        description="Monitor's contrast setting",
        title="Contrast",
        ge=0,
        le=100,
    )
    brightness: Optional[int] = Field(
        ...,
        description="Monitor's brightness setting",
        title="Brightness",
        ge=0,
        le=100,
    )


class WaterDelivery(AindModel):
    """Description of water delivery system"""

    # required fields
    spout_diameter: create_unit_with_value("Spout Diameter", {'value'}, Decimal, SizeUnit, SizeUnit.MM) = Field(..., title="Spout diameter (mm)")
    spout_position: RelativePosition = Field(..., title="Spout stage position")
    water_calibration_values: Dict[str, Any] = Field(..., title="Water calibration values")

    # optional fields
    stage_type: Optional[MotorizedStage] = Field(None, title="Motorized stage")


class MousePlatform(AindModel):
    """Behavior platform for a mouse during a session"""

    track_wheel: Union[Tube, Treadmill, Disc] = Field(..., title="Track wheel type")

    # optional fields
    stage_software: Optional[Software] = Field(None, title="Stage software")
    water_delivery: Optional[WaterDelivery] = Field(None, title="Water delivery")


class VisualStimulusDisplayAssembly(AindModel):
    """Visual display"""

    # required fields
    monitor: Monitor = Field(..., title="Monitor")
    viewing_distance: create_unit_with_value("Viewing Distance", {'value'}, Decimal, SizeUnit, SizeUnit.CM) = Field(..., title="Viewing distance (cm)", units="cm")

    # optional fields
    position: Optional[RelativePosition] = Field(None, title="Relative position of the monitor")
