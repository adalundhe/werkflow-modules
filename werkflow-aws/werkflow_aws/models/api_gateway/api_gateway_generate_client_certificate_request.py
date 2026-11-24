from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGenerateClientCertificateRequest(BaseModel):
    description: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
