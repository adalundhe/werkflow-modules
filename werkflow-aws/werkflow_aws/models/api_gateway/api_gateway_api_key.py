from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayApiKey(BaseModel):
    id: StrictStr | None = None
    value: StrictStr | None = None
    name: StrictStr | None = None
    customerId: StrictStr | None = None
    description: StrictStr | None = None
    enabled: StrictBool | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    stageKeys: list[StrictStr] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
