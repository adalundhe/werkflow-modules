from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetDocumentationPartRequest(BaseModel):
    restApiId: StrictStr
    documentationPartId: StrictStr
