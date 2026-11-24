from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class GlacierDescribeVaultResponse(BaseModel):
    VaultARN: StrictStr | None = None
    VaultName: StrictStr | None = None
    CreationDate: StrictStr | None = None
    LastInventoryDate: StrictStr | None = None
    NumberOfArchives: StrictInt | None = None
    SizeInBytes: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
