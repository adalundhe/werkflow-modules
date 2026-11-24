from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_single_sign_on import DataZoneSingleSignOn


class DataZoneCreateDomainResponse(BaseModel):
    id: StrictStr | None = None
    rootDomainUnitId: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    singleSignOn: DataZoneSingleSignOn | None = None
    domainExecutionRole: StrictStr | None = None
    arn: StrictStr | None = None
    kmsKeyIdentifier: StrictStr | None = None
    status: StrictStr | None = None
    portalUrl: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    domainVersion: StrictStr | None = None
    serviceRole: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
