from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_tag_model import CodeArtifactTagModel


class CodeArtifactCreatePackageGroupRequest(BaseModel):
    domain: StrictStr
    packageGroup: StrictStr
    domainOwner: StrictStr | None = None
    contactInfo: StrictStr | None = None
    description: StrictStr | None = None
    tags: list[CodeArtifactTagModel] | None = None
