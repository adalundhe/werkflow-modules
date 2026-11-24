from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildDeleteFleetRequest(BaseModel):
    arn: StrictStr
