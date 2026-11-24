from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .fms_action_target import FMSActionTarget


class FMSReplaceNetworkAclAssociationAction(BaseModel):
    Description: StrictStr | None = None
    AssociationId: FMSActionTarget | None = None
    NetworkAclId: FMSActionTarget | None = None
    FMSCanRemediate: StrictBool | None = None
