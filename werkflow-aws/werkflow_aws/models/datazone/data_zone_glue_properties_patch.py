from __future__ import annotations
from pydantic import BaseModel
from .data_zone_glue_connection_patch import DataZoneGlueConnectionPatch


class DataZoneGluePropertiesPatch(BaseModel):
    glueConnectionInput: DataZoneGlueConnectionPatch | None = None
