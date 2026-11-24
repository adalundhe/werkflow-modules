from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRUpdatePullThroughCacheRuleRequest(BaseModel):
    ecrRepositoryPrefix: StrictStr
    registryId: StrictStr | None = None
    credentialArn: StrictStr | None = None
    customRoleArn: StrictStr | None = None
