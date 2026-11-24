from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class ECRDeletePullThroughCacheRuleResponse(BaseModel):
    ecrRepositoryPrefix: StrictStr | None = None
    upstreamRegistryUrl: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    registryId: StrictStr | None = None
    credentialArn: StrictStr | None = None
    customRoleArn: StrictStr | None = None
    upstreamRepositoryPrefix: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
