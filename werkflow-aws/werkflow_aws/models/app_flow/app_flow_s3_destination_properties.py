from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_s3_output_format_config import AppFlowS3OutputFormatConfig


class AppFlowS3DestinationProperties(BaseModel):
    bucketName: StrictStr | None = None
    bucketPrefix: StrictStr | None = None
    s3OutputFormatConfig: AppFlowS3OutputFormatConfig | None = None
