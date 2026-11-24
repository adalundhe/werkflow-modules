from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AWSSecretsManagerRotationRules(BaseModel):
    AutomaticallyAfterDays: StrictInt | None = None
    Duration: StrictStr | None = None
    ScheduleExpression: StrictStr | None = None
