from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ConfirmProductInstanceResponse(BaseModel):
    Return: StrictBool | None = None
    OwnerId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
