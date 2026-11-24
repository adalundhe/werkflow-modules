from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kendra_s3_path import KendraS3Path
from .kendra_tag import KendraTag


class KendraCreateFaqRequest(BaseModel):
    IndexId: StrictStr
    Name: StrictStr
    S3Path: KendraS3Path
    RoleArn: StrictStr
    Description: StrictStr | None = None
    Tags: list[KendraTag] | None = None
    FileFormat: Literal['CSV', 'CSV_WITH_HEADER', 'JSON'] | None = None
    ClientToken: StrictStr | None = None
    LanguageCode: StrictStr | None = None
