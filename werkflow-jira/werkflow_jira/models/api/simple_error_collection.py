from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SimpleErrorCollection(BaseModel):
    errorMessages: list[StrictStr] | None = None
    errors: dict[StrictStr, StrictStr] | None = None
    httpStatusCode: StrictInt | None = None
