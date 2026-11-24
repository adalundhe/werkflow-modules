from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GlueS3SourceAdditionalOptions(BaseModel):
    BoundedSize: StrictInt | None = None
    BoundedFiles: StrictInt | None = None
