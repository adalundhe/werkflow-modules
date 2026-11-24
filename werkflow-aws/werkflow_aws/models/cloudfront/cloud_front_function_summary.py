from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_function_config import CloudFrontFunctionConfig
from .cloud_front_function_metadata import CloudFrontFunctionMetadata


class CloudFrontFunctionSummary(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    FunctionConfig: CloudFrontFunctionConfig | None = None
    FunctionMetadata: CloudFrontFunctionMetadata | None = None
