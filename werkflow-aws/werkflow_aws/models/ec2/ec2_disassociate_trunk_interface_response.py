from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisassociateTrunkInterfaceResponse(BaseModel):
    Return: StrictBool | None = None
    ClientToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
