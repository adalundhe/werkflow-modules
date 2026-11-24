from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchServerlessVpcEndpointDetail(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    vpcId: StrictStr | None = None
    subnetIds: list[StrictStr] | None = None
    securityGroupIds: list[StrictStr] | None = None
    status: StrictStr | None = None
    createdDate: StrictInt | None = None
    failureCode: StrictStr | None = None
    failureMessage: StrictStr | None = None
