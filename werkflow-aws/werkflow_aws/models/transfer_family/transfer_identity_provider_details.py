from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferIdentityProviderDetails(BaseModel):
    Url: StrictStr | None = None
    InvocationRole: StrictStr | None = None
    DirectoryId: StrictStr | None = None
    Function: StrictStr | None = None
    SftpAuthenticationMethods: StrictStr | None = None
