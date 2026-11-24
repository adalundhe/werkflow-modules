from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyTransitGatewayMeteringPolicyRequest(BaseModel):
    TransitGatewayMeteringPolicyId: StrictStr
    AddMiddleboxAttachmentIds: list[StrictStr] | None = None
    RemoveMiddleboxAttachmentIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
