from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRedshiftClusterDeferredMaintenanceWindow(BaseModel):
    DeferMaintenanceEndTime: StrictStr | None = None
    DeferMaintenanceIdentifier: StrictStr | None = None
    DeferMaintenanceStartTime: StrictStr | None = None
