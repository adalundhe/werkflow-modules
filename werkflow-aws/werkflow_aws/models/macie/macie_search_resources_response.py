from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_matching_resource import MacieMatchingResource


class MacieSearchResourcesResponse(BaseModel):
    matchingResources: list[MacieMatchingResource] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
