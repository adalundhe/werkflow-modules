from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlacierUploadListElement(BaseModel):
    MultipartUploadId: StrictStr | None = None
    VaultARN: StrictStr | None = None
    ArchiveDescription: StrictStr | None = None
    PartSizeInBytes: StrictInt | None = None
    CreationDate: StrictStr | None = None
