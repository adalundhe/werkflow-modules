from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_client_properties import WorkSpacesClientProperties


class WorkSpacesClientPropertiesResult(BaseModel):
    ResourceId: StrictStr | None = None
    ClientProperties: WorkSpacesClientProperties | None = None
