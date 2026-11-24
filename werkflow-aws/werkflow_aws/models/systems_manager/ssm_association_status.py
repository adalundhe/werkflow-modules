from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SSMAssociationStatus(BaseModel):
    Date: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    Message: StrictStr | None = None
    AdditionalInfo: StrictStr | None = None
