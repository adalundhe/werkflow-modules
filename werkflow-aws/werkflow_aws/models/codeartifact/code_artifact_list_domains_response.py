from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_domain_summary import CodeArtifactDomainSummary


class CodeArtifactListDomainsResponse(BaseModel):
    domains: list[CodeArtifactDomainSummary] | None = None
    nextToken: StrictStr | None = None
