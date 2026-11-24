from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMDeleteResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    PolicyId: StrictStr
    PolicyHash: StrictStr
    DeletionMode: Literal['RemoveSharing', 'RollbackMigration'] | None = None
