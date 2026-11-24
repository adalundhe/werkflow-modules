from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftModifyClusterMaintenanceRequest(BaseModel):
    ClusterIdentifier: StrictStr
    DeferMaintenance: StrictBool | None = None
    DeferMaintenanceIdentifier: StrictStr | None = None
    DeferMaintenanceStartTime: datetime.datetime | StrictStr | None = None
    DeferMaintenanceEndTime: datetime.datetime | StrictStr | None = None
    DeferMaintenanceDuration: StrictInt | None = None
