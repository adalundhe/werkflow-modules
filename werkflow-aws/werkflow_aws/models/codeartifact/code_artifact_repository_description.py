from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from typing import Any
from .code_artifact_upstream_repository import CodeArtifactUpstreamRepository


class CodeArtifactRepositoryDescription(BaseModel):
    name: StrictStr | None = None
    administratorAccount: StrictStr | None = None
    domainName: StrictStr | None = None
    domainOwner: StrictStr | None = None
    arn: StrictStr | None = None
    description: StrictStr | None = None
    upstreams: list[CodeArtifactUpstreamRepository] | None = None
    externalConnections: list[dict[str, Any]] | None = None
    createdTime: datetime.datetime | None = None
