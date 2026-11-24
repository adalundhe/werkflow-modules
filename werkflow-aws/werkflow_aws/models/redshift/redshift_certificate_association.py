from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftCertificateAssociation(BaseModel):
    CustomDomainName: StrictStr | None = None
    ClusterIdentifier: StrictStr | None = None
