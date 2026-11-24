from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_guru_s3_repository_details import CodeGuruS3RepositoryDetails


class CodeGuruS3BucketRepository(BaseModel):
    Name: StrictStr | None = None
    Details: CodeGuruS3RepositoryDetails | None = None
