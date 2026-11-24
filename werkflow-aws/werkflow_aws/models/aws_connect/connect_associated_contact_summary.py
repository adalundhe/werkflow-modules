from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectAssociatedContactSummary(BaseModel):
    ContactId: StrictStr | None = None
    ContactArn: StrictStr | None = None
    InitiationTimestamp: datetime.datetime | StrictStr | None = None
    DisconnectTimestamp: datetime.datetime | StrictStr | None = None
    InitialContactId: StrictStr | None = None
    PreviousContactId: StrictStr | None = None
    RelatedContactId: StrictStr | None = None
    InitiationMethod: StrictStr | None = None
    Channel: StrictStr | None = None
