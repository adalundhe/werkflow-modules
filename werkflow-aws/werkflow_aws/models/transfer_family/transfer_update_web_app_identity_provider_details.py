from __future__ import annotations
from pydantic import BaseModel
from .transfer_update_web_app_identity_center_config import TransferUpdateWebAppIdentityCenterConfig


class TransferUpdateWebAppIdentityProviderDetails(BaseModel):
    IdentityCenterConfig: TransferUpdateWebAppIdentityCenterConfig | None = None
