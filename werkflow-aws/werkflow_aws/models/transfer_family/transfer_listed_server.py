from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TransferListedServer(BaseModel):
    Arn: StrictStr | None = None
    Domain: StrictStr | None = None
    IdentityProviderType: StrictStr | None = None
    EndpointType: StrictStr | None = None
    LoggingRole: StrictStr | None = None
    ServerId: StrictStr | None = None
    State: StrictStr | None = None
    UserCount: StrictInt | None = None
