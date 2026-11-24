from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_streaming_properties import WorkSpacesStreamingProperties


class WorkSpacesModifyStreamingPropertiesRequest(BaseModel):
    ResourceId: StrictStr
    StreamingProperties: WorkSpacesStreamingProperties | None = None
