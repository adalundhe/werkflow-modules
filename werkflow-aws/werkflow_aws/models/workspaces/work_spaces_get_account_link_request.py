from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesGetAccountLinkRequest(BaseModel):
    LinkId: StrictStr | None = None
    LinkedAccountId: StrictStr | None = None
