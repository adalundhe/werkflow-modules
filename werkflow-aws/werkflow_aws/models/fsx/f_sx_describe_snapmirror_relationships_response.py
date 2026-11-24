from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_snapmirror_relationship import FSxSnapmirrorRelationship


class FSxDescribeSnapmirrorRelationshipsResponse(BaseModel):
    SnapmirrorRelationships: list[FSxSnapmirrorRelationship] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
