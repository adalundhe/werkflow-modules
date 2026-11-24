from __future__ import annotations
from pydantic import BaseModel
from .data_zone_lineage_sql_query_run_details import DataZoneLineageSqlQueryRunDetails


class DataZoneLineageRunDetails(BaseModel):
    sqlQueryRunDetails: DataZoneLineageSqlQueryRunDetails | None = None
