from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectWorkspacePage(BaseModel):
    ResourceArn: StrictStr | None = None
    Page: StrictStr | None = None
    Slug: StrictStr | None = None
    InputData: StrictStr | None = None
