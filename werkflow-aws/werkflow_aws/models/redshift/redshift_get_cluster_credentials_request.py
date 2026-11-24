from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftGetClusterCredentialsRequest(BaseModel):
    DbUser: StrictStr
    DbName: StrictStr | None = None
    ClusterIdentifier: StrictStr | None = None
    DurationSeconds: StrictInt | None = None
    AutoCreate: StrictBool | None = None
    DbGroups: list[StrictStr] | None = None
    CustomDomainName: StrictStr | None = None
