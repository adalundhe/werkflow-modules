from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListSubscriptionRequestsRequest(BaseModel):
    domainIdentifier: StrictStr
    status: Literal['PENDING', 'ACCEPTED', 'REJECTED'] | None = None
    subscribedListingId: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    owningIamPrincipalArn: StrictStr | None = None
    approverProjectId: StrictStr | None = None
    owningUserId: StrictStr | None = None
    owningGroupId: StrictStr | None = None
    sortBy: Literal['CREATED_AT', 'UPDATED_AT'] | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
