from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteApplicationStatusCheckRequest(BaseModel):
    ApplicationStatusCheckId: StrictStr
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
