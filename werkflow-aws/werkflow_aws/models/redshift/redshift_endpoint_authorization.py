from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftEndpointAuthorization(BaseModel):
    Grantor: StrictStr | None = None
    Grantee: StrictStr | None = None
    ClusterIdentifier: StrictStr | None = None
    AuthorizeTime: datetime.datetime | StrictStr | None = None
    ClusterStatus: StrictStr | None = None
    Status: StrictStr | None = None
    AllowedAllVPCs: StrictBool | None = None
    AllowedVPCs: list[StrictStr] | None = None
    EndpointCount: StrictInt | None = None
