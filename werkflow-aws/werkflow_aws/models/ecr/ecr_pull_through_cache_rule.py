from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECRPullThroughCacheRule(BaseModel):
    ecrRepositoryPrefix: StrictStr | None = None
    upstreamRegistryUrl: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    registryId: StrictStr | None = None
    credentialArn: StrictStr | None = None
    customRoleArn: StrictStr | None = None
    upstreamRepositoryPrefix: StrictStr | None = None
    upstreamRegistry: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
