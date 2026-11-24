from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CognitoIDPAccountTakeoverActionType(BaseModel):
    Notify: StrictBool | None = None
    EventAction: StrictStr | None = None
