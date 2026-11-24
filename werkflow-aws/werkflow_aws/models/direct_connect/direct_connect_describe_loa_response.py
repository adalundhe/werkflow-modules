from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class DirectConnectDescribeLoaResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    loaContent: StrictBytes | Any | None = None
    loaContentType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
