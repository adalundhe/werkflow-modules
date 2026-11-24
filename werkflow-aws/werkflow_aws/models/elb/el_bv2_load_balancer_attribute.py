from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2LoadBalancerAttribute(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
