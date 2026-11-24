from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECRDescribeRepositoriesRequest(BaseModel):
    registryId: StrictStr | None = None
    repositoryNames: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
