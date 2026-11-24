from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_idp_client_secret_input import QuickSightIdpClientSecretInput


class QuickSightClientSecretConfigurationDetail(BaseModel):
    Idp: QuickSightIdpClientSecretInput | None = None
