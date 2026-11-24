from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMServiceSpecificCredential(BaseModel):
    CreateDate: datetime.datetime | StrictStr | None = None
    ExpirationDate: datetime.datetime | StrictStr | None = None
    ServiceName: StrictStr | None = None
    ServiceUserName: StrictStr | None = None
    ServicePassword: StrictStr | None = None
    ServiceCredentialAlias: StrictStr | None = None
    ServiceCredentialSecret: StrictStr | None = None
    ServiceSpecificCredentialId: StrictStr | None = None
    UserName: StrictStr | None = None
    Status: StrictStr | None = None
