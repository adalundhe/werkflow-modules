from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2BlockPublicAccessStates(BaseModel):
    InternetGatewayBlockMode: StrictStr | None = None
