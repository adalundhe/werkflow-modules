from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EndUserMessagingConditionalValidation(BaseModel):
    MinLength: StrictInt | None = None
    MaxLength: StrictInt | None = None
    Pattern: StrictStr | None = None
    AllowedValues: list[StrictStr] | None = None
