from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_guru_code_artifacts import CodeGuruCodeArtifacts


class CodeGuruS3RepositoryDetails(BaseModel):
    BucketName: StrictStr | None = None
    CodeArtifacts: CodeGuruCodeArtifacts | None = None
