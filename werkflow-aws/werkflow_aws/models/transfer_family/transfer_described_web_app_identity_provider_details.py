from __future__ import annotations
from pydantic import BaseModel
from .transfer_described_identity_center_config import TransferDescribedIdentityCenterConfig


class TransferDescribedWebAppIdentityProviderDetails(BaseModel):
    IdentityCenterConfig: TransferDescribedIdentityCenterConfig | None = None
