from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowS3InputFormatConfig(BaseModel):
    s3InputFileType: StrictStr | None = None
