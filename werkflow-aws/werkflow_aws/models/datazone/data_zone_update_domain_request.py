from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_single_sign_on import DataZoneSingleSignOn


class DataZoneUpdateDomainRequest(BaseModel):
    identifier: StrictStr
    description: StrictStr | None = None
    singleSignOn: DataZoneSingleSignOn | None = None
    domainExecutionRole: StrictStr | None = None
    serviceRole: StrictStr | None = None
    name: StrictStr | None = None
    clientToken: StrictStr | None = None
