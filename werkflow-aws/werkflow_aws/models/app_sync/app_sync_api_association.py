from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncApiAssociation(BaseModel):
    domainName: StrictStr | None = None
    apiId: StrictStr | None = None
    associationStatus: StrictStr | None = None
    deploymentDetail: StrictStr | None = None
