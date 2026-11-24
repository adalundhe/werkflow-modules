from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CognitoIDPTermsDescriptionType(BaseModel):
    TermsId: StrictStr | None = None
    TermsName: StrictStr | None = None
    Enforcement: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
