from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportJobDataSourceCredentialPair(BaseModel):
    Username: StrictStr | None = None
    Password: StrictStr | None = None
