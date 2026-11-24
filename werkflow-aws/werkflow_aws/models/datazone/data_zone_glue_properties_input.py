from __future__ import annotations
from pydantic import BaseModel
from .data_zone_glue_connection_input import DataZoneGlueConnectionInput


class DataZoneGluePropertiesInput(BaseModel):
    glueConnectionInput: DataZoneGlueConnectionInput | None = None
