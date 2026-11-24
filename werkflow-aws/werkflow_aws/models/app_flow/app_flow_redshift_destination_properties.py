from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_error_handling_config import AppFlowErrorHandlingConfig


class AppFlowRedshiftDestinationProperties(BaseModel):
    object: StrictStr | None = None
    intermediateBucketName: StrictStr | None = None
    bucketPrefix: StrictStr | None = None
    errorHandlingConfig: AppFlowErrorHandlingConfig | None = None
