from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesConnectClientAddIn(BaseModel):
    AddInId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    Name: StrictStr | None = None
    URL: StrictStr | None = None
