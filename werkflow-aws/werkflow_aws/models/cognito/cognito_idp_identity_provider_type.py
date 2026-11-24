from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CognitoIDPIdentityProviderType(BaseModel):
    UserPoolId: StrictStr | None = None
    ProviderName: StrictStr | None = None
    ProviderType: StrictStr | None = None
    ProviderDetails: dict[StrictStr, StrictStr] | None = None
    AttributeMapping: dict[StrictStr, StrictStr] | None = None
    IdpIdentifiers: list[StrictStr] | None = None
    AcrMapping: dict[StrictStr, StrictStr] | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
