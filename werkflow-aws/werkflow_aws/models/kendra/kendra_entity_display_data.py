from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraEntityDisplayData(BaseModel):
    UserName: StrictStr | None = None
    GroupName: StrictStr | None = None
    IdentifiedUserName: StrictStr | None = None
    FirstName: StrictStr | None = None
    LastName: StrictStr | None = None
