from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_cloud_watch_output_config import SSMCloudWatchOutputConfig


class SSMGetCommandInvocationResponse(BaseModel):
    CommandId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    Comment: StrictStr | None = None
    DocumentName: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    PluginName: StrictStr | None = None
    ResponseCode: StrictInt | None = None
    ExecutionStartDateTime: StrictStr | None = None
    ExecutionElapsedTime: StrictStr | None = None
    ExecutionEndDateTime: StrictStr | None = None
    Status: StrictStr | None = None
    StatusDetails: StrictStr | None = None
    StandardOutputContent: StrictStr | None = None
    StandardOutputUrl: StrictStr | None = None
    StandardErrorContent: StrictStr | None = None
    StandardErrorUrl: StrictStr | None = None
    CloudWatchOutputConfig: SSMCloudWatchOutputConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
