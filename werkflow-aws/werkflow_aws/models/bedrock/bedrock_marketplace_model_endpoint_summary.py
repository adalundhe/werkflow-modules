from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockMarketplaceModelEndpointSummary(BaseModel):
    endpointArn: StrictStr | None = None
    modelSourceIdentifier: StrictStr | None = None
    status: StrictStr | None = None
    statusMessage: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
