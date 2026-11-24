from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_s3_path import KendraS3Path
from .kendra_tag import KendraTag


class KendraCreateQuerySuggestionsBlockListRequest(BaseModel):
    IndexId: StrictStr
    Name: StrictStr
    SourceS3Path: KendraS3Path
    RoleArn: StrictStr
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
    Tags: list[KendraTag] | None = None
