from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_s3_path import KendraS3Path


class KendraUpdateQuerySuggestionsBlockListRequest(BaseModel):
    IndexId: StrictStr
    Id: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    SourceS3Path: KendraS3Path | None = None
    RoleArn: StrictStr | None = None
