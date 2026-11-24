from __future__ import annotations
from pydantic import BaseModel
from .data_zone_redshift_cluster_storage import DataZoneRedshiftClusterStorage
from .data_zone_redshift_serverless_storage import DataZoneRedshiftServerlessStorage


class DataZoneRedshiftStorage(BaseModel):
    redshiftClusterSource: DataZoneRedshiftClusterStorage | None = None
    redshiftServerlessSource: DataZoneRedshiftServerlessStorage | None = None
