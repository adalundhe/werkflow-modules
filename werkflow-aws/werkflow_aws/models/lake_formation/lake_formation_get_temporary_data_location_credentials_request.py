from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .lake_formation_audit_context import LakeFormationAuditContext


class LakeFormationGetTemporaryDataLocationCredentialsRequest(BaseModel):
    DurationSeconds: StrictInt | None = None
    AuditContext: LakeFormationAuditContext | None = None
    DataLocations: list[StrictStr] | None = None
    CredentialsScope: Literal['READ', 'READWRITE'] | None = None
