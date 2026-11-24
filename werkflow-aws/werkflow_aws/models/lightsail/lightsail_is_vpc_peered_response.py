from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool


class LightsailIsVpcPeeredResponse(BaseModel):
    isPeered: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
