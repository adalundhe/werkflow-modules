from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_automatic_tape_creation_rule import StorageGatewayAutomaticTapeCreationRule


class StorageGatewayAutomaticTapeCreationPolicyInfo(BaseModel):
    AutomaticTapeCreationRules: list[StorageGatewayAutomaticTapeCreationRule] | None = None
    GatewayARN: StrictStr | None = None
