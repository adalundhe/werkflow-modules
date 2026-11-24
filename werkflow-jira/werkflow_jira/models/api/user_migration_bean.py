from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UserMigrationBean(BaseModel):
    accountId: StrictStr | None = None
    key: StrictStr | None = None
    username: StrictStr | None = None
