from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
