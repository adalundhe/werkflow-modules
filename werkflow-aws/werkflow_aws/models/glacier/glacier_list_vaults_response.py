from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glacier_describe_vault_output import GlacierDescribeVaultOutput


class GlacierListVaultsResponse(BaseModel):
    VaultList: list[GlacierDescribeVaultOutput] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
