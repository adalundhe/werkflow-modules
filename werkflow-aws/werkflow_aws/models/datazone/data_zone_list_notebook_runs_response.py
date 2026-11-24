from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_notebook_run_summary import DataZoneNotebookRunSummary


class DataZoneListNotebookRunsResponse(BaseModel):
    items: list[DataZoneNotebookRunSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
