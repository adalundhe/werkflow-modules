from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .eks_repair_action import EKSRepairAction


class EKSNodeRepairConfigOverrides(BaseModel):
    nodeMonitoringCondition: StrictStr | None = None
    nodeUnhealthyReason: StrictStr | None = None
    minRepairWaitTimeMins: StrictInt | None = None
    repairAction: EKSRepairAction | None = None
