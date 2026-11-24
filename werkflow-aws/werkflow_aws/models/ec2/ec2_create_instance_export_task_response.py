from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_export_task import EC2ExportTask


class EC2CreateInstanceExportTaskResponse(BaseModel):
    ExportTask: EC2ExportTask | None = None
    ResponseMetadata: dict[str, Any] | None = None
