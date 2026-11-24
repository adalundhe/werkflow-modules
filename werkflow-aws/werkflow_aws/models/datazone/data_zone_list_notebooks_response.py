from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_notebook_summary import DataZoneNotebookSummary


class DataZoneListNotebooksResponse(BaseModel):
    items: list[DataZoneNotebookSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
