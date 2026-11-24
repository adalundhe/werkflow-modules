from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchKeyStoreAccessOption(BaseModel):
    KeyAccessRoleArn: StrictStr | None = None
    KeyStoreAccessEnabled: StrictBool | None = None
