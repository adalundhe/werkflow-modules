from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeCustomDomainAssociationsRequest(BaseModel):
    CustomDomainName: StrictStr | None = None
    CustomDomainCertificateArn: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
