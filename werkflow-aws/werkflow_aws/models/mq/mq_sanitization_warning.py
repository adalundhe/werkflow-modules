from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQSanitizationWarning(BaseModel):
    AttributeName: StrictStr | None = None
    ElementName: StrictStr | None = None
    Reason: StrictStr | None = None
