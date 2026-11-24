from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_pipeline_error_details import CodePipelineErrorDetails


class CodePipelineRuleExecution(BaseModel):
    ruleExecutionId: StrictStr | None = None
    status: StrictStr | None = None
    summary: StrictStr | None = None
    lastStatusChange: datetime.datetime | StrictStr | None = None
    token: StrictStr | None = None
    lastUpdatedBy: StrictStr | None = None
    externalExecutionId: StrictStr | None = None
    externalExecutionUrl: StrictStr | None = None
    errorDetails: CodePipelineErrorDetails | None = None
