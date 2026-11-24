from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetDocumentationVersionRequest(BaseModel):
    restApiId: StrictStr
    documentationVersion: StrictStr
