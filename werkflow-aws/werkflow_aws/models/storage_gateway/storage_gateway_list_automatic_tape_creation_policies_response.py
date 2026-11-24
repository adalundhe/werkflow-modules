from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .storage_gateway_automatic_tape_creation_policy_info import StorageGatewayAutomaticTapeCreationPolicyInfo


class StorageGatewayListAutomaticTapeCreationPoliciesResponse(BaseModel):
    AutomaticTapeCreationPolicyInfos: list[StorageGatewayAutomaticTapeCreationPolicyInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
