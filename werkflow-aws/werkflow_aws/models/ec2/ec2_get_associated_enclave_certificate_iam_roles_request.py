from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetAssociatedEnclaveCertificateIamRolesRequest(BaseModel):
    CertificateArn: StrictStr
    DryRun: StrictBool | None = None
