from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class GlacierUploadArchiveRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    vaultName: StrictStr
    accountId: StrictStr
    archiveDescription: StrictStr | None = None
    checksum: StrictStr | None = None
    body: StrictBytes | BinaryIO | StrictStr | None = None
