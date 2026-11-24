from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CognitoIDPProviderDescription(BaseModel):
    ProviderName: StrictStr | None = None
    ProviderType: StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
