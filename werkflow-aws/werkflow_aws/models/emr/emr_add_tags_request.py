from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_tag import EMRTag


class EMRAddTagsRequest(BaseModel):
    ResourceId: StrictStr
    Tags: list[EMRTag]
    ClusterId: StrictStr | None = None
