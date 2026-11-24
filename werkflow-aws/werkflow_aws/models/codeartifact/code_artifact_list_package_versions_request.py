from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from werkflow_aws.types.codeartifact_format import CodeArtifactFormat


class CodeArtifactListPackageVersionsRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    format: CodeArtifactFormat
    package: StrictStr
    domainOwner: StrictStr | None = None
    namespace: StrictStr | None = None
    status: StrictStr | None = None
    sortBy: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
