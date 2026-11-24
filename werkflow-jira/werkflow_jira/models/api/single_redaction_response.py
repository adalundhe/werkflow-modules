from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SingleRedactionResponse(BaseModel):
    externalId: StrictStr | None = None
    successful: StrictBool | None = None
