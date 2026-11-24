from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeArtifactListRepositoriesRequest(BaseModel):
    repositoryPrefix: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
