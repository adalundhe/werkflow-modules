from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_error_detail import GlueErrorDetail


class GlueBatchStopJobRunError(BaseModel):
    JobName: StrictStr | None = None
    JobRunId: StrictStr | None = None
    ErrorDetail: GlueErrorDetail | None = None
