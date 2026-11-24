from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2InstanceMetadataDefaultsResponse(BaseModel):
    HttpTokens: StrictStr | None = None
    HttpPutResponseHopLimit: StrictInt | None = None
    HttpEndpoint: StrictStr | None = None
    InstanceMetadataTags: StrictStr | None = None
    ManagedBy: StrictStr | None = None
    ManagedExceptionMessage: StrictStr | None = None
    HttpTokensEnforced: StrictStr | None = None
