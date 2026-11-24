from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .emr_release_label_filter import EMRReleaseLabelFilter


class EMRListReleaseLabelsRequest(BaseModel):
    Filters: EMRReleaseLabelFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
