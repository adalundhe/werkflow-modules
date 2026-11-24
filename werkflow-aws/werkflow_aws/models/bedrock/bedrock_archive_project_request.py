from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockArchiveProjectRequest(BaseModel):
    projectIdentifier: StrictStr
