from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_function_summary import CloudFrontFunctionSummary


class CloudFrontTestResult(BaseModel):
    FunctionSummary: CloudFrontFunctionSummary | None = None
    ComputeUtilization: StrictStr | None = None
    FunctionExecutionLogs: list[StrictStr] | None = None
    FunctionErrorMessage: StrictStr | None = None
    FunctionOutput: StrictStr | None = None
