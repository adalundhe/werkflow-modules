from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_update_target import RedshiftUpdateTarget


class RedshiftMaintenanceTrack(BaseModel):
    MaintenanceTrackName: StrictStr | None = None
    DatabaseVersion: StrictStr | None = None
    UpdateTargets: list[RedshiftUpdateTarget] | None = None
