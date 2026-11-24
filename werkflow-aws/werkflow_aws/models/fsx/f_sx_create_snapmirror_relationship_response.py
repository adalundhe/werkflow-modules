from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_snapmirror_relationship import FSxSnapmirrorRelationship


class FSxCreateSnapmirrorRelationshipResponse(BaseModel):
    SnapmirrorRelationship: FSxSnapmirrorRelationship | None = None
    ResponseMetadata: dict[str, Any] | None = None
