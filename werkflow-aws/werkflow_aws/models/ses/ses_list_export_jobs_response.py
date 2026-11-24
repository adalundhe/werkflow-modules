from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_export_job_summary import SESExportJobSummary


class SESListExportJobsResponse(BaseModel):
    ExportJobs: list[SESExportJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
