from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsApplicationMaintenanceConfigurationDescription(BaseModel):
    ApplicationMaintenanceWindowStartTime: StrictStr | None = None
    ApplicationMaintenanceWindowEndTime: StrictStr | None = None
