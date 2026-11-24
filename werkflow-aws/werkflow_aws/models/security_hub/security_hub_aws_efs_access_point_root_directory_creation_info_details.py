from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEfsAccessPointRootDirectoryCreationInfoDetails(BaseModel):
    OwnerGid: StrictStr | None = None
    OwnerUid: StrictStr | None = None
    Permissions: StrictStr | None = None
