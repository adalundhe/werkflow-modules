from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_function_config import CloudFrontFunctionConfig


class CloudFrontConnectionFunctionSummary(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    ConnectionFunctionConfig: CloudFrontFunctionConfig | None = None
    ConnectionFunctionArn: StrictStr | None = None
    Status: StrictStr | None = None
    Stage: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
