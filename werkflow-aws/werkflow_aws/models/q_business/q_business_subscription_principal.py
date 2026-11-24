from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessSubscriptionPrincipal(BaseModel):
    user: StrictStr | None = None
    group: StrictStr | None = None
