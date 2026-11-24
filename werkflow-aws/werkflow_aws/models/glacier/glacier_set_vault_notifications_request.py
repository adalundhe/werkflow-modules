from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glacier_vault_notification_config import GlacierVaultNotificationConfig


class GlacierSetVaultNotificationsRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    vaultNotificationConfig: GlacierVaultNotificationConfig | None = None
