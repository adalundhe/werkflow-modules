from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_upsolver_s3_output_format_config import AppFlowUpsolverS3OutputFormatConfig


class AppFlowUpsolverDestinationProperties(BaseModel):
    bucketName: StrictStr | None = None
    bucketPrefix: StrictStr | None = None
    s3OutputFormatConfig: AppFlowUpsolverS3OutputFormatConfig | None = None
