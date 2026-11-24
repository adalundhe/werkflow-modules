from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_s3_path import KendraS3Path
from .kendra_tag import KendraTag


class KendraCreateThesaurusRequest(BaseModel):
    IndexId: StrictStr
    Name: StrictStr
    RoleArn: StrictStr
    SourceS3Path: KendraS3Path
    Description: StrictStr | None = None
    Tags: list[KendraTag] | None = None
    ClientToken: StrictStr | None = None
