from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool


class EC2RestoreImageFromRecycleBinResponse(BaseModel):
    Return: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
