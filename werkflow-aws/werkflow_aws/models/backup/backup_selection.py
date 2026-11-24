from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_condition import BackupCondition
from .backup_conditions import BackupConditions


class BackupSelection(BaseModel):
    SelectionName: StrictStr | None = None
    IamRoleArn: StrictStr | None = None
    Resources: list[StrictStr] | None = None
    ListOfTags: list[BackupCondition] | None = None
    NotResources: list[StrictStr] | None = None
    Conditions: BackupConditions | None = None
