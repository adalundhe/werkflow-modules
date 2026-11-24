from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_control_input_parameter import BackupControlInputParameter
from .backup_control_scope import BackupControlScope


class BackupFrameworkControl(BaseModel):
    ControlName: StrictStr | None = None
    ControlInputParameters: list[BackupControlInputParameter] | None = None
    ControlScope: BackupControlScope | None = None
