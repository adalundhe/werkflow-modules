from __future__ import annotations
from pydantic import BaseModel
from .data_zone_metadata_form_reference import DataZoneMetadataFormReference


class DataZoneMetadataFormEnforcementDetail(BaseModel):
    requiredMetadataForms: list[DataZoneMetadataFormReference] | None = None
