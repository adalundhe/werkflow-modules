from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_s3_location import CodePipelineS3Location


class CodePipelineArtifactDetail(BaseModel):
    name: StrictStr | None = None
    s3location: CodePipelineS3Location | None = None
