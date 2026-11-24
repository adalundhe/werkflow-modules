from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ClassicLoadBalancer(BaseModel):
    Name: StrictStr | None = None
