from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GetDateFieldResponse(BaseModel):
    dateCustomFieldId: StrictInt | None = None
    type: StrictStr | None = None
