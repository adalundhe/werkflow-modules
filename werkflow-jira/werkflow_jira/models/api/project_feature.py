from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ProjectFeature(BaseModel):
    feature: StrictStr | None = None
    imageUri: StrictStr | None = None
    localisedDescription: StrictStr | None = None
    localisedName: StrictStr | None = None
    prerequisites: list[StrictStr] | None = None
    projectId: StrictInt | None = None
    state: StrictStr | None = None
    toggleLocked: StrictBool | None = None
