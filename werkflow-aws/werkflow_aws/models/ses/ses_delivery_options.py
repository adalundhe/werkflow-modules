from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SESDeliveryOptions(BaseModel):
    TlsPolicy: StrictStr | None = None
    SendingPoolName: StrictStr | None = None
    MaxDeliverySeconds: StrictInt | None = None
    SharedPoolDeliveryMode: StrictStr | None = None
