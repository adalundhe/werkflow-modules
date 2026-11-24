from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_s3_input_format_config import AppFlowS3InputFormatConfig


class AppFlowS3SourceProperties(BaseModel):
    bucketName: StrictStr | None = None
    bucketPrefix: StrictStr | None = None
    s3InputFormatConfig: AppFlowS3InputFormatConfig | None = None
