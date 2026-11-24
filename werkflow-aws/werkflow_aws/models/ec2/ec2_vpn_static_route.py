from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VpnStaticRoute(BaseModel):
    DestinationCidrBlock: StrictStr | None = None
    Source: StrictStr | None = None
    State: StrictStr | None = None
