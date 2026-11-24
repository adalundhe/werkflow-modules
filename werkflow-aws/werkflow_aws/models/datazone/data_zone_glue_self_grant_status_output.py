from __future__ import annotations
from pydantic import BaseModel
from .data_zone_self_grant_status_detail import DataZoneSelfGrantStatusDetail


class DataZoneGlueSelfGrantStatusOutput(BaseModel):
    selfGrantStatusDetails: list[DataZoneSelfGrantStatusDetail] | None = None
