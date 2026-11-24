from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectQuickConnectContactData(BaseModel):
    ContactId: StrictStr | None = None
    InitiationTimestamp: datetime.datetime | StrictStr | None = None
    QuickConnectId: StrictStr | None = None
    QuickConnectName: StrictStr | None = None
    QuickConnectType: StrictStr | None = None
