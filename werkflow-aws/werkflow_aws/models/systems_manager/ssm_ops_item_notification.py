from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMOpsItemNotification(BaseModel):
    Arn: StrictStr | None = None
