from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glacier_vault_access_policy import GlacierVaultAccessPolicy


class GlacierGetVaultAccessPolicyResponse(BaseModel):
    policy: GlacierVaultAccessPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
