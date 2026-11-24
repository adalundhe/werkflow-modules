from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class RedshiftModifyCustomDomainAssociationResponse(BaseModel):
    CustomDomainName: StrictStr | None = None
    CustomDomainCertificateArn: StrictStr | None = None
    ClusterIdentifier: StrictStr | None = None
    CustomDomainCertExpiryTime: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
