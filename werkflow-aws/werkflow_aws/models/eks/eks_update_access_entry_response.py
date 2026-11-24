from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .eks_access_entry import EKSAccessEntry


class EKSUpdateAccessEntryResponse(BaseModel):
    accessEntry: EKSAccessEntry | None = None
    ResponseMetadata: dict[str, Any] | None = None
