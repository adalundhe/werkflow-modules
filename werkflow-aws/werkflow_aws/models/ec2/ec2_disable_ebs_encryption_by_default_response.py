from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool


class EC2DisableEbsEncryptionByDefaultResponse(BaseModel):
    EbsEncryptionByDefault: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
