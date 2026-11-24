from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateContactFlowAliasResponse(BaseModel):
    ContactFlowArn: StrictStr | None = None
    Id: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
