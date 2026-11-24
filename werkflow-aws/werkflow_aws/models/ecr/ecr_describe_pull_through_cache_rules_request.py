from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECRDescribePullThroughCacheRulesRequest(BaseModel):
    registryId: StrictStr | None = None
    ecrRepositoryPrefixes: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
