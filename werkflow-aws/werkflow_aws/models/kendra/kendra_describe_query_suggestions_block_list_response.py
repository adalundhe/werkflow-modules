from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .kendra_s3_path import KendraS3Path


class KendraDescribeQuerySuggestionsBlockListResponse(BaseModel):
    IndexId: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    SourceS3Path: KendraS3Path | None = None
    ItemCount: StrictInt | None = None
    FileSizeBytes: StrictInt | None = None
    RoleArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
