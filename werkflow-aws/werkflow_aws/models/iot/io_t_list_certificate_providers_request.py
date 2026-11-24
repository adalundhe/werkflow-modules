from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTListCertificateProvidersRequest(BaseModel):
    nextToken: StrictStr | None = None
    ascendingOrder: StrictBool | None = None
