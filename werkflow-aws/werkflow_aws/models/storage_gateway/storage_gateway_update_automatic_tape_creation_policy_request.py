from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_automatic_tape_creation_rule import StorageGatewayAutomaticTapeCreationRule


class StorageGatewayUpdateAutomaticTapeCreationPolicyRequest(BaseModel):
    AutomaticTapeCreationRules: list[StorageGatewayAutomaticTapeCreationRule]
    GatewayARN: StrictStr
