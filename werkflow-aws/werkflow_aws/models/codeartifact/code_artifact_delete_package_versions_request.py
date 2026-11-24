from __future__ import annotations
from pydantic import BaseModel, StrictStr
from werkflow_aws.types.codeartifact_format import CodeArtifactFormat


class CodeArtifactDeletePackageVersionsRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    format: CodeArtifactFormat
    package: StrictStr
    versions: list[StrictStr]
    domainOwner: StrictStr | None = None
    namespace: StrictStr | None = None
    expectedStatus: StrictStr | None = None
