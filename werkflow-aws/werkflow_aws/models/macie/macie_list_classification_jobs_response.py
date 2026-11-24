from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_job_summary import MacieJobSummary


class MacieListClassificationJobsResponse(BaseModel):
    items: list[MacieJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
