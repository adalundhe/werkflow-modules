from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from werkflow_aws.types.codeartifact_format import CodeArtifactFormat


class CodeArtifactListPackagesRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    domainOwner: StrictStr | None = None
    format: CodeArtifactFormat | None = None
    namespace: StrictStr | None = None
    packagePrefix: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
