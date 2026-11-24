from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayCreateDocumentationVersionRequest(BaseModel):
    restApiId: StrictStr
    documentationVersion: StrictStr
    stageName: StrictStr | None = None
    description: StrictStr | None = None
