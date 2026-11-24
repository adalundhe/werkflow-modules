from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KMSAliasListEntry(BaseModel):
    AliasName: StrictStr | None = None
    AliasArn: StrictStr | None = None
    TargetKeyId: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastUpdatedDate: datetime.datetime | StrictStr | None = None
