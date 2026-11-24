from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightVpcConnectionProperties(BaseModel):
    VpcConnectionArn: StrictStr | None = None
