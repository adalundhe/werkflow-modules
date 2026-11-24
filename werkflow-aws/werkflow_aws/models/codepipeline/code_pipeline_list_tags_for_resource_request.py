from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodePipelineListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
