from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class ECRUpdatePullThroughCacheRuleResponse(BaseModel):
    ecrRepositoryPrefix: StrictStr | None = None
    registryId: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    credentialArn: StrictStr | None = None
    customRoleArn: StrictStr | None = None
    upstreamRepositoryPrefix: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
