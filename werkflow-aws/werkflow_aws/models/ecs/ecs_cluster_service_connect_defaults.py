from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSClusterServiceConnectDefaults(BaseModel):
    namespace: StrictStr | None = None
