from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AcmeAccount(BaseModel):
    AccountUrl: StrictStr | None = None
    PublicKeyThumbprint: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    AcmeExternalAccountBindingArn: StrictStr | None = None
    Contacts: list[StrictStr] | None = None
