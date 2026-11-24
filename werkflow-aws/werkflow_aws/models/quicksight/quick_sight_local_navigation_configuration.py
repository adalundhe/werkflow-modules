from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightLocalNavigationConfiguration(BaseModel):
    TargetSheetId: StrictStr | None = None
