from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListDomainConfigurationsRequest(BaseModel):
    marker: StrictStr | None = None
    pageSize: StrictInt | None = None
    serviceType: Literal['DATA', 'CREDENTIAL_PROVIDER', 'JOBS'] | None = None
