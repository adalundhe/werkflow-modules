from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_artifact_repository_external_connection_info import CodeArtifactRepositoryExternalConnectionInfo
from .code_artifact_upstream_repository_info import CodeArtifactUpstreamRepositoryInfo


class CodeArtifactRepositoryDescriptionModel(BaseModel):
    name: StrictStr | None = None
    administratorAccount: StrictStr | None = None
    domainName: StrictStr | None = None
    domainOwner: StrictStr | None = None
    arn: StrictStr | None = None
    description: StrictStr | None = None
    upstreams: list[CodeArtifactUpstreamRepositoryInfo] | None = None
    externalConnections: list[CodeArtifactRepositoryExternalConnectionInfo] | None = None
    createdTime: datetime.datetime | StrictStr | None = None
