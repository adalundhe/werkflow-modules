from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_tag import CodeArtifactTag


class CodeArtifactCreateDomainRequest(BaseModel):
    domain: StrictStr
    encryptionKey: StrictStr | None = None
    tags: list[CodeArtifactTag] | None = None
