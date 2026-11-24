from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildDeleteProjectRequest(BaseModel):
    name: StrictStr
