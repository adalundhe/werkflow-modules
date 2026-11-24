from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaDeadLetterConfig(BaseModel):
    TargetArn: StrictStr | None = None
