from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerCoreNetworkPolicyVersion(BaseModel):
    CoreNetworkId: StrictStr | None = None
    PolicyVersionId: StrictInt | None = None
    Alias: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    ChangeSetState: StrictStr | None = None
