from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_error_details import CodePipelineErrorDetails


class CodePipelineActionExecution(BaseModel):
    actionExecutionId: StrictStr | None = None
    status: StrictStr | None = None
    summary: StrictStr | None = None
    lastStatusChange: datetime.datetime | StrictStr | None = None
    token: StrictStr | None = None
    lastUpdatedBy: StrictStr | None = None
    externalExecutionId: StrictStr | None = None
    externalExecutionUrl: StrictStr | None = None
    percentComplete: StrictInt | None = None
    errorDetails: CodePipelineErrorDetails | None = None
    logStreamARN: StrictStr | None = None
