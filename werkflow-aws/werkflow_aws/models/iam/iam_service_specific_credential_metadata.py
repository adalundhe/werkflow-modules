from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMServiceSpecificCredentialMetadata(BaseModel):
    UserName: StrictStr | None = None
    Status: StrictStr | None = None
    ServiceUserName: StrictStr | None = None
    ServiceCredentialAlias: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    ExpirationDate: datetime.datetime | StrictStr | None = None
    ServiceSpecificCredentialId: StrictStr | None = None
    ServiceName: StrictStr | None = None
