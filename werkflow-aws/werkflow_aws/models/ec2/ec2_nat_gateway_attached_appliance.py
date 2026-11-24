from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2NatGatewayAttachedAppliance(BaseModel):
    Type: StrictStr | None = None
    ApplianceArn: StrictStr | None = None
    VpcEndpointId: StrictStr | None = None
    AttachmentState: StrictStr | None = None
    ModificationState: StrictStr | None = None
    FailureCode: StrictStr | None = None
    FailureMessage: StrictStr | None = None
