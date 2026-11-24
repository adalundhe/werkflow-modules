from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_export_task import RDSExportTask


class RDSDescribeExportTasksResponse(BaseModel):
    Marker: StrictStr | None = None
    ExportTasks: list[RDSExportTask] | None = None
    ResponseMetadata: dict[str, Any] | None = None
