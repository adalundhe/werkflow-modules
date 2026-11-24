from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .fms_action_target import FMSActionTarget


class FMSCreateNetworkAclAction(BaseModel):
    Description: StrictStr | None = None
    Vpc: FMSActionTarget | None = None
    FMSCanRemediate: StrictBool | None = None
