from __future__ import annotations
from pydantic import BaseModel
from .backup_condition_parameter import BackupConditionParameter


class BackupConditions(BaseModel):
    StringEquals: list[BackupConditionParameter] | None = None
    StringNotEquals: list[BackupConditionParameter] | None = None
    StringLike: list[BackupConditionParameter] | None = None
    StringNotLike: list[BackupConditionParameter] | None = None
