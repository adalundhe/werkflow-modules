from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointEventStream(BaseModel):
    ApplicationId: StrictStr | None = None
    DestinationStreamArn: StrictStr | None = None
    ExternalId: StrictStr | None = None
    LastModifiedDate: StrictStr | None = None
    LastUpdatedBy: StrictStr | None = None
    RoleArn: StrictStr | None = None
