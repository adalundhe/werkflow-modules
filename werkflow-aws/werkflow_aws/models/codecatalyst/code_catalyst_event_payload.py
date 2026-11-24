from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystEventPayload(BaseModel):
    contentType: StrictStr | None = None
    data: StrictStr | None = None
