from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUploadUrlMetadata(BaseModel):
    Url: StrictStr | None = None
    UrlExpiry: StrictStr | None = None
    HeadersToInclude: dict[StrictStr, StrictStr] | None = None
