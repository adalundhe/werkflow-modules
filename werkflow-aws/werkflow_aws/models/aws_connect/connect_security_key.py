from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectSecurityKey(BaseModel):
    AssociationId: StrictStr | None = None
    Key: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
