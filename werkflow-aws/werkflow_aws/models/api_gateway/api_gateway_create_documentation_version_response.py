from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayCreateDocumentationVersionResponse(BaseModel):
    version: StrictStr | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
