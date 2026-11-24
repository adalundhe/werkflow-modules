from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool
from .f_sx_autocommit_period import FSxAutocommitPeriod
from .f_sx_snaplock_retention_period import FSxSnaplockRetentionPeriod


class FSxCreateSnaplockConfiguration(BaseModel):
    SnaplockType: Literal['COMPLIANCE', 'ENTERPRISE']
    AuditLogVolume: StrictBool | None = None
    AutocommitPeriod: FSxAutocommitPeriod | None = None
    PrivilegedDelete: Literal['DISABLED', 'ENABLED', 'PERMANENTLY_DISABLED'] | None = None
    RetentionPeriod: FSxSnaplockRetentionPeriod | None = None
    VolumeAppendModeEnabled: StrictBool | None = None
