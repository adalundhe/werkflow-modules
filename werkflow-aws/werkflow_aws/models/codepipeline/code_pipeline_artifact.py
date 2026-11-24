from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_artifact_location import CodePipelineArtifactLocation


class CodePipelineArtifact(BaseModel):
    name: StrictStr | None = None
    revision: StrictStr | None = None
    location: CodePipelineArtifactLocation | None = None
