from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupConditionParameter(BaseModel):
    ConditionKey: StrictStr | None = None
    ConditionValue: StrictStr | None = None
