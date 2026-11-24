from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockRuntimeModelStreamErrorException(BaseModel):
    message: StrictStr | None = None
    originalStatusCode: StrictInt | None = None
    originalMessage: StrictStr | None = None
