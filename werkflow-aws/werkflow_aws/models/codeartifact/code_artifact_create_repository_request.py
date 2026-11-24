from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_tag import CodeArtifactTag
from .code_artifact_upstream_repository import CodeArtifactUpstreamRepository


class CodeArtifactCreateRepositoryRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    domainOwner: StrictStr | None = None
    description: StrictStr | None = None
    upstreams: list[CodeArtifactUpstreamRepository] | None = None
    tags: list[CodeArtifactTag] | None = None
