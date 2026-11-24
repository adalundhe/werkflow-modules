from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZoneCreateFormTypeResponse(BaseModel):
    domainId: StrictStr | None = None
    name: StrictStr | None = None
    revision: StrictStr | None = None
    description: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    originDomainId: StrictStr | None = None
    originProjectId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
