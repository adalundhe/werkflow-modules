from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListCertificatesByCARequest(BaseModel):
    caCertificateId: StrictStr
    pageSize: StrictInt | None = None
    marker: StrictStr | None = None
    ascendingOrder: StrictBool | None = None
