from __future__ import annotations
from pydantic import BaseModel
from .code_artifact_domain_description import CodeArtifactDomainDescription


class CodeArtifactDomainResponse(BaseModel):
    domain: CodeArtifactDomainDescription | None = None
