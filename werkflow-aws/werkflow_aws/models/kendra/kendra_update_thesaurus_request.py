from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_s3_path import KendraS3Path


class KendraUpdateThesaurusRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    RoleArn: StrictStr | None = None
    SourceS3Path: KendraS3Path | None = None
