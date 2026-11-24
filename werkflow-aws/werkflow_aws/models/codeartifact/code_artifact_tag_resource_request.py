from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_tag_model import CodeArtifactTagModel


class CodeArtifactTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[CodeArtifactTagModel]
