from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyEc2ImageDetails(BaseModel):
    ImageArn: StrictStr | None = None
