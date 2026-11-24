from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteCustomDomainAssociationRequest(BaseModel):
    ClusterIdentifier: StrictStr
    CustomDomainName: StrictStr
