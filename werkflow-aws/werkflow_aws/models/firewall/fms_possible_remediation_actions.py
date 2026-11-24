from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_possible_remediation_action import FMSPossibleRemediationAction


class FMSPossibleRemediationActions(BaseModel):
    Description: StrictStr | None = None
    Actions: list[FMSPossibleRemediationAction] | None = None
