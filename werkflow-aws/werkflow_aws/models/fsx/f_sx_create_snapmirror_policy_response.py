from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_snapmirror_policy import FSxSnapmirrorPolicy


class FSxCreateSnapmirrorPolicyResponse(BaseModel):
    SnapmirrorPolicy: FSxSnapmirrorPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
