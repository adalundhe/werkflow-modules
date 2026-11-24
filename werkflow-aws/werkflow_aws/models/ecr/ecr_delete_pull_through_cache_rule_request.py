from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRDeletePullThroughCacheRuleRequest(BaseModel):
    ecrRepositoryPrefix: StrictStr
    registryId: StrictStr | None = None
