from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftCreateCustomDomainAssociationRequest(BaseModel):
    CustomDomainName: StrictStr
    CustomDomainCertificateArn: StrictStr
    ClusterIdentifier: StrictStr
