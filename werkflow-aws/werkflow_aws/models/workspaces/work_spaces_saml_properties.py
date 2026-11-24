from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesSamlProperties(BaseModel):
    Status: StrictStr | None = None
    UserAccessUrl: StrictStr | None = None
    RelayStateParameterName: StrictStr | None = None
