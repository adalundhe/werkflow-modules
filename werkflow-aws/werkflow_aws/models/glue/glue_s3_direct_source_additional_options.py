from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class GlueS3DirectSourceAdditionalOptions(BaseModel):
    BoundedSize: StrictInt | None = None
    BoundedFiles: StrictInt | None = None
    EnableSamplePath: StrictBool | None = None
    SamplePath: StrictStr | None = None
