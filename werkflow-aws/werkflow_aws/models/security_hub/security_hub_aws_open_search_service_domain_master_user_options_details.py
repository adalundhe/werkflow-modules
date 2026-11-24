from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsOpenSearchServiceDomainMasterUserOptionsDetails(BaseModel):
    MasterUserArn: StrictStr | None = None
    MasterUserName: StrictStr | None = None
    MasterUserPassword: StrictStr | None = None
