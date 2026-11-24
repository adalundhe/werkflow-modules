from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteDocumentationPartRequest(BaseModel):
    restApiId: StrictStr
    documentationPartId: StrictStr
