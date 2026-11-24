from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CancelImportTaskRequest(BaseModel):
    CancelReason: StrictStr | None = None
    DryRun: StrictBool | None = None
    ImportTaskId: StrictStr | None = None
