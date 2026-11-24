from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class ECRValidatePullThroughCacheRuleResponse(BaseModel):
    ecrRepositoryPrefix: StrictStr | None = None
    registryId: StrictStr | None = None
    upstreamRegistryUrl: StrictStr | None = None
    credentialArn: StrictStr | None = None
    customRoleArn: StrictStr | None = None
    upstreamRepositoryPrefix: StrictStr | None = None
    isValid: StrictBool | None = None
    failure: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
