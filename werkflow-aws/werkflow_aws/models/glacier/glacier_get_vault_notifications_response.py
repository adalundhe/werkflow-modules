from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glacier_vault_notification_config import GlacierVaultNotificationConfig


class GlacierGetVaultNotificationsResponse(BaseModel):
    vaultNotificationConfig: GlacierVaultNotificationConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
