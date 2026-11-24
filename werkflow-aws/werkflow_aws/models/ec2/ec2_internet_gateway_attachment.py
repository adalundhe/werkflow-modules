from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InternetGatewayAttachment(BaseModel):
    State: StrictStr | None = None
    VpcId: StrictStr | None = None
