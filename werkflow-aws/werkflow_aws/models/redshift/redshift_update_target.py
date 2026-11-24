from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_supported_operation import RedshiftSupportedOperation


class RedshiftUpdateTarget(BaseModel):
    MaintenanceTrackName: StrictStr | None = None
    DatabaseVersion: StrictStr | None = None
    SupportedOperations: list[RedshiftSupportedOperation] | None = None
