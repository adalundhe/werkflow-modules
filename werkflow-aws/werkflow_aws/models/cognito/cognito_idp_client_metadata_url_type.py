from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CognitoIDPClientMetadataURLType(BaseModel):
    URL: StrictStr | None = None
    CachedDate: datetime.datetime | StrictStr | None = None
    ExpirationDate: datetime.datetime | StrictStr | None = None
