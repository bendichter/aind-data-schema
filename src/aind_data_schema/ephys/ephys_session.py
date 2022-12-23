""" ephys session description and related objects """

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import Field

from ..base import AindCoreModel, AindModel
from .ephys_rig import Coordinates3d, SizeUnit


class SessionType(Enum):
    """Session type name"""

    TEST = "Test"
    OPTO = "Optotagging"
    VISUAL_ORIENTATION = "Visual Orientation"


class ExpectedDataStream(Enum):
    """Names of data streams to expect in recording"""

    NEUROPIXELS_PROBES = "Neuropixels probes"
    BODY_CAMERA = "Body camera"
    FACE_CAMERA = "Face camera"
    EYE_CAMERA = "Eye camera"
    BONSAI_FILE = "Bonsai file"
    HARP_FILE = "Harp bin file"
    OTHER = "Other"


class CcfVersion(Enum):
    """CCF version"""

    CCFv3 = "CCFv3"


class CcfCoords(AindModel):
    """Coordinates in CCF template space"""

    ml: float = Field(..., title="ML")
    ap: float = Field(..., title="AP")
    dv: float = Field(..., title="DV")
    unit: SizeUnit = Field(SizeUnit.UM, title="Coordinate unit")
    ccf_version: CcfVersion = Field(CcfVersion.CCFv3, title="CCF version")


class Laser(AindModel):
    """Description of a laser's session configuration"""

    name: str = Field(..., title="Name")
    wavelength: int = Field(..., title="Wavelength")
    wavelength_unit: SizeUnit = Field(SizeUnit.NM, title="Wavelength unit")
    power: float = Field(..., title="Power")
    ower_unit: str = Field("milliwatt", title="Maximum power unit")
    manipulator_coordinates: Coordinates3d = Field(
        ...,
        title="Manipulator coordinates",
    )
    targeted_structure: Optional[str] = Field(None, title="Targeted structure")
    targeted_ccf_coordinates: Optional[CcfCoords] = Field(
        None,
        title="Targeted CCF coordinates",
    )


class EphysProbe(AindModel):
    """Description of an ephys probe"""

    name: str = Field(..., title="Name")
    tip_targeted_structure: str
    manipulator_coordinates: Coordinates3d = Field(
        ...,
        title="Manipulator coordinates",
    )
    other_targeted_structures: Optional[List[str]] = None
    targeted_ccf_coordinates: Optional[CcfCoords] = Field(
        None,
        title="Targeted CCF coordinates",
    )


class Stream(AindModel):
    """Stream of data with a start and stop time"""

    stream_start_time: datetime = Field(..., title="Stream start time")
    stream_stop_time: datetime = Field(..., title="Stream stop time")
    probes: Optional[List[EphysProbe]] = Field(
        None, title="Probes", unique_items=True
    )
    lasers: Optional[List[Laser]] = Field(
        None, title="Lasers", unique_items=True
    )


class EphysSession(AindCoreModel):
    """Description of an ephys recording session"""

    schema_version: str = Field(
        "0.3.0", description="schema version", title="Version", const=True
    )
    experimenter_full_name: str = Field(
        ...,
        description="First and last name of the experimenter.",
        title="Experimenter full name",
    )
    session_start_time: datetime = Field(..., title="Session start time")
    session_end_time: datetime = Field(..., title="Session end time")
    subject_id: int = Field(..., title="Subject ID")
    session_type: SessionType = Field(..., title="Session type")
    session_description: Optional[str] = Field(
        None, title="Session description"
    )
    stimulus_protocol_id: Optional[str] = Field(
        None, title="Stimulus protocol ID"
    )
    iacuc_protocol: Optional[str] = Field(None, title="IACUC protocol")
    rig_id: str = Field(..., title="Rig ID")
    expected_data_streams: Optional[List[ExpectedDataStream]] = Field(
        None, title="Expected data streams"
    )
    probe_streams: List[Stream] = Field(
        ..., title="Probe streams", unique_items=True
    )
    ccf_coordinate_transform: Optional[str] = Field(
        None,
        description="Path to file that details the CCF-to-lab coordinate transform.",
        title="CCF coordinate transform",
    )
    notes: Optional[str] = None
