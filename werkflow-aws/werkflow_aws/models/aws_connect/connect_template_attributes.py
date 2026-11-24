from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectTemplateAttributes(BaseModel):
    CustomAttributes: dict[StrictStr, StrictStr] | None = None
    CustomerProfileAttributes: StrictStr | None = None
