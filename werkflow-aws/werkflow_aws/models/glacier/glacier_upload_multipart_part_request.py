from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class GlacierUploadMultipartPartRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    accountId: StrictStr
    vaultName: StrictStr
    uploadId: StrictStr
    checksum: StrictStr | None = None
    range: StrictStr | None = None
    body: StrictBytes | BinaryIO | StrictStr | None = None
