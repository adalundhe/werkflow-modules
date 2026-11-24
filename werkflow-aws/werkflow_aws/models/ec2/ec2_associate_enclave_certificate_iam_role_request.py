from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateEnclaveCertificateIamRoleRequest(BaseModel):
    CertificateArn: StrictStr
    RoleArn: StrictStr
    DryRun: StrictBool | None = None
