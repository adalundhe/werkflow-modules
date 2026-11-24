from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2ModifyInstanceMaintenanceOptionsResponse(BaseModel):
    InstanceId: StrictStr | None = None
    AutoRecovery: StrictStr | None = None
    RebootMigration: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
