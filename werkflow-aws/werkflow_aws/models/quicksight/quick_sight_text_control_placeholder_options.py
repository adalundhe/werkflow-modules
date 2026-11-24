from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTextControlPlaceholderOptions(BaseModel):
    Visibility: StrictStr | None = None
