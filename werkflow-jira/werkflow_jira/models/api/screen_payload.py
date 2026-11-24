from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier
from .tab_payload import TabPayload


class ScreenPayload(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    tabs: list[TabPayload] | None = None
