from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftRecommendedAction(BaseModel):
    Text: StrictStr | None = None
    Database: StrictStr | None = None
    Command: StrictStr | None = None
    Type: StrictStr | None = None
