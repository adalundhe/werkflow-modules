from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CognitoIDPTermsType(BaseModel):
    TermsId: StrictStr | None = None
    UserPoolId: StrictStr | None = None
    ClientId: StrictStr | None = None
    TermsName: StrictStr | None = None
    TermsSource: StrictStr | None = None
    Enforcement: StrictStr | None = None
    Links: dict[StrictStr, StrictStr] | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
