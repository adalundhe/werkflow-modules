from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchServerlessUpdateVpcEndpointDetail(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    subnetIds: list[StrictStr] | None = None
    securityGroupIds: list[StrictStr] | None = None
    lastModifiedDate: StrictInt | None = None
