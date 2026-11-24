from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_maintenance_track import RedshiftMaintenanceTrack


class RedshiftDescribeClusterTracksResponse(BaseModel):
    MaintenanceTracks: list[RedshiftMaintenanceTrack] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
