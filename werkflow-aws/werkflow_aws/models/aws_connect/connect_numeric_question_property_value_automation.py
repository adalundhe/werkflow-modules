from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectNumericQuestionPropertyValueAutomation(BaseModel):
    Label: StrictStr | None = None
