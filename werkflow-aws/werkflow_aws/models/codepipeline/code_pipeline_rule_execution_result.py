from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_error_details import CodePipelineErrorDetails


class CodePipelineRuleExecutionResult(BaseModel):
    externalExecutionId: StrictStr | None = None
    externalExecutionSummary: StrictStr | None = None
    externalExecutionUrl: StrictStr | None = None
    errorDetails: CodePipelineErrorDetails | None = None
