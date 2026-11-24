from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMDescribePatchPropertiesResponse(BaseModel):
    Properties: list[dict[StrictStr, StrictStr]] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
