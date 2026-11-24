from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CognitoIDPUICustomizationType(BaseModel):
    UserPoolId: StrictStr | None = None
    ClientId: StrictStr | None = None
    ImageUrl: StrictStr | None = None
    CSS: StrictStr | None = None
    CSSVersion: StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
