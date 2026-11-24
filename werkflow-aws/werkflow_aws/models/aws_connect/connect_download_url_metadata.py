from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDownloadUrlMetadata(BaseModel):
    Url: StrictStr | None = None
    UrlExpiry: StrictStr | None = None
