from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class APIGatewayDocumentationVersion(BaseModel):
    version: StrictStr | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
