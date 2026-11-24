from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AmplifyListArtifactsRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
    jobId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
