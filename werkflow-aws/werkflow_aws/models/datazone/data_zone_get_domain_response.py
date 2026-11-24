from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_delete_progress import DataZoneDeleteProgress
from .data_zone_failure_reason import DataZoneFailureReason
from .data_zone_single_sign_on import DataZoneSingleSignOn


class DataZoneGetDomainResponse(BaseModel):
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
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    domainVersion: StrictStr | None = None
    serviceRole: StrictStr | None = None
    failureReasons: list[DataZoneFailureReason] | None = None
    deleteProgress: DataZoneDeleteProgress | None = None
    ResponseMetadata: dict[str, Any] | None = None
