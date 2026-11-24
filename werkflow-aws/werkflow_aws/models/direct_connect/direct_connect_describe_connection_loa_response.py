from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .direct_connect_loa import DirectConnectLoa


class DirectConnectDescribeConnectionLoaResponse(BaseModel):
    loa: DirectConnectLoa | None = None
    ResponseMetadata: dict[str, Any] | None = None
