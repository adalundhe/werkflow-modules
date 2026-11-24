from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrderOfCustomFieldOptions(BaseModel):
    after: StrictStr | None = None
    customFieldOptionIds: list[StrictStr] | None = None
    position: StrictStr | None = None
