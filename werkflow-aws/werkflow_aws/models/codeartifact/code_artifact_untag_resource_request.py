from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
