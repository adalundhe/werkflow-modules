from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .status_scope import StatusScope


class JiraStatus(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    scope: StatusScope | None = None
    statusCategory: StrictStr | None = None
