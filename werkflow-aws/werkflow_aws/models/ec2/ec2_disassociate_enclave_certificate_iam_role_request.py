from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisassociateEnclaveCertificateIamRoleRequest(BaseModel):
    CertificateArn: StrictStr
    RoleArn: StrictStr
    DryRun: StrictBool | None = None
