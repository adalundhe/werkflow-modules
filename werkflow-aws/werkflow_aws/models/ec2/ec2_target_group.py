from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TargetGroup(BaseModel):
    Arn: StrictStr | None = None
