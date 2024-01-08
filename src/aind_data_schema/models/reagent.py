"""Classes to define reagents"""

from datetime import date
from typing import Optional

from pydantic import Field

from aind_data_schema.base import AindModel
from aind_data_schema.models.pid_names import PIDName
from aind_data_schema.models.institutions import Institution


class Reagent(AindModel):
    """Description of reagent used in procedure"""

    name: str = Field(..., title="Name")
    source: Institution.ONE_OF = Field(..., title="Source")
    rrid: Optional[PIDName] = Field(None, title="Research Resource ID")
    lot_number: str = Field(..., title="Lot number")
    expiration_date: Optional[date] = Field(None, title="Lot expiration date")
