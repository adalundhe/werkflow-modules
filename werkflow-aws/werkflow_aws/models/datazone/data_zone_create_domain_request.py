from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_single_sign_on import DataZoneSingleSignOn


class DataZoneCreateDomainRequest(BaseModel):
    name: StrictStr
    description: StrictStr | None = None
    singleSignOn: DataZoneSingleSignOn | None = None
    domainExecutionRole: StrictStr | None = None
    kmsKeyIdentifier: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    domainVersion: Literal['V1', 'V2'] | None = None
    serviceRole: StrictStr | None = None
    clientToken: StrictStr | None = None
