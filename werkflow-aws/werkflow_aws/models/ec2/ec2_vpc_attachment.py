from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VpcAttachment(BaseModel):
    VpcId: StrictStr | None = None
    State: StrictStr | None = None
