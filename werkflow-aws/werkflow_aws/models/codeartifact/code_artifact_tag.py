from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactTag(BaseModel):
    key: StrictStr
    value: StrictStr
