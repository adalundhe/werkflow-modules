from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_trust import DirectoryServiceTrust


class DirectoryServiceDescribeTrustsResponse(BaseModel):
    Trusts: list[DirectoryServiceTrust] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
