from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_policy_version import IoTPolicyVersion


class IoTListPolicyVersionsResponse(BaseModel):
    policyVersions: list[IoTPolicyVersion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
