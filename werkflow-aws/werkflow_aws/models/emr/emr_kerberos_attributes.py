from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRKerberosAttributes(BaseModel):
    Realm: StrictStr | None = None
    KdcAdminPassword: StrictStr | None = None
    CrossRealmTrustPrincipalPassword: StrictStr | None = None
    ADDomainJoinUser: StrictStr | None = None
    ADDomainJoinPassword: StrictStr | None = None
