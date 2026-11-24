from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_addon_details import GuardDutyAddonDetails


class GuardDutyCoverageEksClusterDetails(BaseModel):
    ClusterName: StrictStr | None = None
    CoveredNodes: StrictInt | None = None
    CompatibleNodes: StrictInt | None = None
    AddonDetails: GuardDutyAddonDetails | None = None
    ManagementType: StrictStr | None = None
