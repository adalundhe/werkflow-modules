from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCatalystListDevEnvironmentSessionsRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    devEnvironmentId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
