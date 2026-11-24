from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_s3_artifact_location import CodePipelineS3ArtifactLocation


class CodePipelineArtifactLocation(BaseModel):
    type: StrictStr | None = None
    s3Location: CodePipelineS3ArtifactLocation | None = None
