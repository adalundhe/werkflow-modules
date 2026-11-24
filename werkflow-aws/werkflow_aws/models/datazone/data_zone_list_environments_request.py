from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListEnvironmentsRequest(BaseModel):
    domainIdentifier: StrictStr
    projectIdentifier: StrictStr
    awsAccountId: StrictStr | None = None
    status: Literal['ACTIVE', 'CREATING', 'UPDATING', 'DELETING', 'CREATE_FAILED', 'UPDATE_FAILED', 'DELETE_FAILED', 'VALIDATION_FAILED', 'SUSPENDED', 'DISABLED', 'EXPIRED', 'DELETED', 'INACCESSIBLE'] | None = None
    awsAccountRegion: StrictStr | None = None
    environmentProfileIdentifier: StrictStr | None = None
    environmentBlueprintIdentifier: StrictStr | None = None
    provider: StrictStr | None = None
    name: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
