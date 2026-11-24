from __future__ import annotations
from pydantic import BaseModel
from .transfer_identity_center_config import TransferIdentityCenterConfig


class TransferWebAppIdentityProviderDetails(BaseModel):
    IdentityCenterConfig: TransferIdentityCenterConfig | None = None
