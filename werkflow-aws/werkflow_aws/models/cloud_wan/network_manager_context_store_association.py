from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class NetworkManagerContextStoreAssociation(BaseModel):
    ContextStoreId: StrictStr | None = None
    TransitGatewayArn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
