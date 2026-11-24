from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_addon_info import EKSAddonInfo


class EKSDescribeAddonVersionsResponse(BaseModel):
    addons: list[EKSAddonInfo] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
