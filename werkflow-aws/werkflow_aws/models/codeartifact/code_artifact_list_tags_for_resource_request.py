from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
