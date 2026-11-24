from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class APIGatewayV2ProductPageSummaryNoBody(BaseModel):
    LastModified: datetime.datetime | StrictStr | None = None
    PageTitle: StrictStr | None = None
    ProductPageArn: StrictStr | None = None
    ProductPageId: StrictStr | None = None
