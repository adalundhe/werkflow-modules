from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_auto_termination_policy import EMRAutoTerminationPolicy


class EMRGetAutoTerminationPolicyResponse(BaseModel):
    AutoTerminationPolicy: EMRAutoTerminationPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
