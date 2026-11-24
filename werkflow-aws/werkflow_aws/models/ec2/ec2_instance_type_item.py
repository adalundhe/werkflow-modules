from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceTypeItem(BaseModel):
    InstanceType: StrictStr | None = None
