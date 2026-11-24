from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDocumentationPartLocation(BaseModel):
    type: StrictStr | None = None
    path: StrictStr | None = None
    method: StrictStr | None = None
    statusCode: StrictStr | None = None
    name: StrictStr | None = None
