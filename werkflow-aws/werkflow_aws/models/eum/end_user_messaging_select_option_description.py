from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingSelectOptionDescription(BaseModel):
    Option: StrictStr | None = None
    Title: StrictStr | None = None
    Description: StrictStr | None = None
