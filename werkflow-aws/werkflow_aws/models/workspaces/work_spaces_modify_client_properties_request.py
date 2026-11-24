from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_client_properties import WorkSpacesClientProperties


class WorkSpacesModifyClientPropertiesRequest(BaseModel):
    ResourceId: StrictStr
    ClientProperties: WorkSpacesClientProperties
