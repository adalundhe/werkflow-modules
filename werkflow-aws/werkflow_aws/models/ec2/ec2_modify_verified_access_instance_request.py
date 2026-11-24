from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVerifiedAccessInstanceRequest(BaseModel):
    VerifiedAccessInstanceId: StrictStr
    Description: StrictStr | None = None
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
    CidrEndpointsCustomSubDomain: StrictStr | None = None
