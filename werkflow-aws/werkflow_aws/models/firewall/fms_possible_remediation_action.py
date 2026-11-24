from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .fms_remediation_action_with_order import FMSRemediationActionWithOrder


class FMSPossibleRemediationAction(BaseModel):
    Description: StrictStr | None = None
    OrderedRemediationActions: list[FMSRemediationActionWithOrder] | None = None
    IsDefaultAction: StrictBool | None = None
