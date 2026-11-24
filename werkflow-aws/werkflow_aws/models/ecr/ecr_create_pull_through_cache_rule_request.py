from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECRCreatePullThroughCacheRuleRequest(BaseModel):
    ecrRepositoryPrefix: StrictStr
    upstreamRegistryUrl: StrictStr
    registryId: StrictStr | None = None
    upstreamRegistry: Literal['ecr', 'ecr-public', 'quay', 'k8s', 'docker-hub', 'github-container-registry', 'azure-container-registry', 'gitlab-container-registry', 'chainguard'] | None = None
    credentialArn: StrictStr | None = None
    customRoleArn: StrictStr | None = None
    upstreamRepositoryPrefix: StrictStr | None = None
