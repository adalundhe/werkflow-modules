from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftGetClusterCredentialsWithIAMRequest(BaseModel):
    DbName: StrictStr | None = None
    ClusterIdentifier: StrictStr | None = None
    DurationSeconds: StrictInt | None = None
    CustomDomainName: StrictStr | None = None
