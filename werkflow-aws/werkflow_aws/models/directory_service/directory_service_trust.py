from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceTrust(BaseModel):
    DirectoryId: StrictStr | None = None
    TrustId: StrictStr | None = None
    RemoteDomainName: StrictStr | None = None
    TrustType: StrictStr | None = None
    TrustDirection: StrictStr | None = None
    TrustState: StrictStr | None = None
    CreatedDateTime: datetime.datetime | StrictStr | None = None
    LastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    StateLastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    TrustStateReason: StrictStr | None = None
    SelectiveAuth: StrictStr | None = None
