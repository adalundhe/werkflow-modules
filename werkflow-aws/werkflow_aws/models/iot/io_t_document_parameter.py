from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTDocumentParameter(BaseModel):
    key: StrictStr | None = None
    description: StrictStr | None = None
    regex: StrictStr | None = None
    example: StrictStr | None = None
    optional: StrictBool | None = None
