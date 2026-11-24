from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayGetClientCertificateResponse(BaseModel):
    clientCertificateId: StrictStr | None = None
    description: StrictStr | None = None
    pemEncodedCertificate: StrictStr | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    expirationDate: datetime.datetime | StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
