from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PrivateDnsDetails(BaseModel):
    PrivateDnsName: StrictStr | None = None
