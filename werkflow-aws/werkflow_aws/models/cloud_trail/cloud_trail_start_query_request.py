from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailStartQueryRequest(BaseModel):
    QueryStatement: StrictStr | None = None
    DeliveryS3Uri: StrictStr | None = None
    QueryAlias: StrictStr | None = None
    QueryParameters: list[StrictStr] | None = None
    EventDataStoreOwnerAccountId: StrictStr | None = None
