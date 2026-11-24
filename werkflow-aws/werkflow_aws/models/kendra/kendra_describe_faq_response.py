from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_s3_path import KendraS3Path


class KendraDescribeFaqResponse(BaseModel):
    Id: StrictStr | None = None
    IndexId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    S3Path: KendraS3Path | None = None
    Status: StrictStr | None = None
    RoleArn: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    FileFormat: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
