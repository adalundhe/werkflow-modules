from __future__ import annotations
from pydantic import BaseModel
from .data_zone_lineage_run_details import DataZoneLineageRunDetails


class DataZoneJobRunDetails(BaseModel):
    lineageRunDetails: DataZoneLineageRunDetails | None = None
