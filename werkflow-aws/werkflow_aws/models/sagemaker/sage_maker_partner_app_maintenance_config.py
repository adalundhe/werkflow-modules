from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerPartnerAppMaintenanceConfig(BaseModel):
    MaintenanceWindowStart: StrictStr | None = None
