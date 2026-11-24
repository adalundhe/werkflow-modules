from __future__ import annotations
from pydantic import BaseModel
from .data_zone_glue_self_grant_status_output import DataZoneGlueSelfGrantStatusOutput
from .data_zone_redshift_self_grant_status_output import DataZoneRedshiftSelfGrantStatusOutput


class DataZoneSelfGrantStatusOutput(BaseModel):
    glueSelfGrantStatus: DataZoneGlueSelfGrantStatusOutput | None = None
    redshiftSelfGrantStatus: DataZoneRedshiftSelfGrantStatusOutput | None = None
