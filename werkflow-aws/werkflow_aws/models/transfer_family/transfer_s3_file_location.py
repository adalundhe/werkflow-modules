from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferS3FileLocation(BaseModel):
    Bucket: StrictStr | None = None
    Key: StrictStr | None = None
    VersionId: StrictStr | None = None
    Etag: StrictStr | None = None
