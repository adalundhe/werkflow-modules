from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportJobThemeOverrideParameters(BaseModel):
    ThemeId: StrictStr | None = None
    Name: StrictStr | None = None
