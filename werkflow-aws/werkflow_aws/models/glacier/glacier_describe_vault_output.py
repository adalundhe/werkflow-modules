from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlacierDescribeVaultOutput(BaseModel):
    VaultARN: StrictStr | None = None
    VaultName: StrictStr | None = None
    CreationDate: StrictStr | None = None
    LastInventoryDate: StrictStr | None = None
    NumberOfArchives: StrictInt | None = None
    SizeInBytes: StrictInt | None = None
