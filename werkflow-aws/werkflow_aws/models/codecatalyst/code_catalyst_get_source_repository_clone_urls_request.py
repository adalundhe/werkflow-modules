from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystGetSourceRepositoryCloneUrlsRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    sourceRepositoryName: StrictStr
