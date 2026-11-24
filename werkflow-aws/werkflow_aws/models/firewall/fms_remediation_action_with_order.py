from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .fms_remediation_action import FMSRemediationAction


class FMSRemediationActionWithOrder(BaseModel):
    RemediationAction: FMSRemediationAction | None = None
    Order: StrictInt | None = None
