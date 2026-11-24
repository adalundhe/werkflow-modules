from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetProjectRequest(BaseModel):
    projectIdentifier: StrictStr
