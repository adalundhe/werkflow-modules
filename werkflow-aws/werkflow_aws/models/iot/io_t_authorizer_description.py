from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class IoTAuthorizerDescription(BaseModel):
    authorizerName: StrictStr | None = None
    authorizerArn: StrictStr | None = None
    authorizerFunctionArn: StrictStr | None = None
    tokenKeyName: StrictStr | None = None
    tokenSigningPublicKeys: dict[StrictStr, StrictStr] | None = None
    status: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    signingDisabled: StrictBool | None = None
    enableCachingForHttp: StrictBool | None = None
