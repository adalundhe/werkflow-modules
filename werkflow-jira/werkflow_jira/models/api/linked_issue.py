from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fields import Fields


class LinkedIssue(BaseModel):
    fields: Fields | None = None
    id: StrictStr | None = None
    key: StrictStr | None = None
    self: StrictStr | None = None
