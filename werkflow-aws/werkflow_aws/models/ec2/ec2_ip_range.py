from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpRange(BaseModel):
    Description: StrictStr | None = None
    CidrIp: StrictStr | None = None
