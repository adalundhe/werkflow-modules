from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class APIGatewayV2PortalProductSummary(BaseModel):
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    PortalProductArn: StrictStr | None = None
    PortalProductId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
