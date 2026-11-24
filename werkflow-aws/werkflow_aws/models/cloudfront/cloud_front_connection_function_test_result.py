from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_connection_function_summary import CloudFrontConnectionFunctionSummary


class CloudFrontConnectionFunctionTestResult(BaseModel):
    ConnectionFunctionSummary: CloudFrontConnectionFunctionSummary | None = None
    ComputeUtilization: StrictStr | None = None
    ConnectionFunctionExecutionLogs: list[StrictStr] | None = None
    ConnectionFunctionErrorMessage: StrictStr | None = None
    ConnectionFunctionOutput: StrictStr | None = None
