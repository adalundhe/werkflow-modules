from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EndUserMessagingSelectValidation(BaseModel):
    MinChoices: StrictInt | None = None
    MaxChoices: StrictInt | None = None
    Options: list[StrictStr] | None = None
