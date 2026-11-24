from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_execution_preview import SSMExecutionPreview


class SSMGetExecutionPreviewResponse(BaseModel):
    ExecutionPreviewId: StrictStr | None = None
    EndedAt: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    ExecutionPreview: SSMExecutionPreview | None = None
    ResponseMetadata: dict[str, Any] | None = None
