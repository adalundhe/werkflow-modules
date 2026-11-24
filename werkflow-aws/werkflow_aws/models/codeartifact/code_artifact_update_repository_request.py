from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_upstream_repository_model import CodeArtifactUpstreamRepositoryModel


class CodeArtifactUpdateRepositoryRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    domainOwner: StrictStr | None = None
    description: StrictStr | None = None
    upstreams: list[CodeArtifactUpstreamRepositoryModel] | None = None
