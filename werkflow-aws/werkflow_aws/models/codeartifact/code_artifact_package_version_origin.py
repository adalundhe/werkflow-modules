from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_domain_entry_point import CodeArtifactDomainEntryPoint


class CodeArtifactPackageVersionOrigin(BaseModel):
    domainEntryPoint: CodeArtifactDomainEntryPoint | None = None
    originType: StrictStr | None = None
