from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchMasterUserOptions(BaseModel):
    MasterUserARN: StrictStr | None = None
    MasterUserName: StrictStr | None = None
    MasterUserPassword: StrictStr | None = None
