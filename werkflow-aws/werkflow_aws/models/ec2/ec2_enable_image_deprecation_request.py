from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableImageDeprecationRequest(BaseModel):
    ImageId: StrictStr
    DeprecateAt: datetime.datetime | StrictStr
    DryRun: StrictBool | None = None
