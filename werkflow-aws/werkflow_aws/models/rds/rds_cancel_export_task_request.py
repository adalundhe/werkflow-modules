from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSCancelExportTaskRequest(BaseModel):
    ExportTaskIdentifier: StrictStr
