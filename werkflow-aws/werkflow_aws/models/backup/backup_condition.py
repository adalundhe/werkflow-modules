from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupCondition(BaseModel):
    ConditionType: StrictStr | None = None
    ConditionKey: StrictStr | None = None
    ConditionValue: StrictStr | None = None
