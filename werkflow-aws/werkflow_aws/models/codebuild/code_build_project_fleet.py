from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildProjectFleet(BaseModel):
    fleetArn: StrictStr | None = None
