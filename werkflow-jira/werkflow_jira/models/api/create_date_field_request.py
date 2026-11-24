from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CreateDateFieldRequest(BaseModel):
    dateCustomFieldId: StrictInt | None = None
    type: StrictStr | None = None
