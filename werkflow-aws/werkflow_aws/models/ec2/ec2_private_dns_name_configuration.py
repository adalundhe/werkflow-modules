from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PrivateDnsNameConfiguration(BaseModel):
    State: StrictStr | None = None
    Type: StrictStr | None = None
    Value: StrictStr | None = None
    Name: StrictStr | None = None
