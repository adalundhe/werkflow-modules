from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerAWSLocation(BaseModel):
    Zone: StrictStr | None = None
    SubnetArn: StrictStr | None = None
