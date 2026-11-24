from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQActionRequired(BaseModel):
    ActionRequiredCode: StrictStr | None = None
    ActionRequiredInfo: StrictStr | None = None
