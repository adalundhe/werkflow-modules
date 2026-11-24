from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyInstanceMaintenanceOptionsRequest(BaseModel):
    InstanceId: StrictStr
    AutoRecovery: Literal['disabled', 'default'] | None = None
    RebootMigration: Literal['disabled', 'default'] | None = None
    DryRun: StrictBool | None = None
