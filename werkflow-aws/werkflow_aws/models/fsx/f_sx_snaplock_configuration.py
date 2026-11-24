from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .f_sx_autocommit_period import FSxAutocommitPeriod
from .f_sx_snaplock_retention_period import FSxSnaplockRetentionPeriod


class FSxSnaplockConfiguration(BaseModel):
    AuditLogVolume: StrictBool | None = None
    AutocommitPeriod: FSxAutocommitPeriod | None = None
    PrivilegedDelete: StrictStr | None = None
    RetentionPeriod: FSxSnaplockRetentionPeriod | None = None
    SnaplockType: StrictStr | None = None
    VolumeAppendModeEnabled: StrictBool | None = None
