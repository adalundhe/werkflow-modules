from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SESPutConfigurationSetDeliveryOptionsRequest(BaseModel):
    ConfigurationSetName: StrictStr
    TlsPolicy: Literal['REQUIRE', 'OPTIONAL'] | None = None
    SendingPoolName: StrictStr | None = None
    MaxDeliverySeconds: StrictInt | None = None
    SharedPoolDeliveryMode: Literal['GLOBAL', 'REGIONAL', 'ACCOUNT'] | None = None
