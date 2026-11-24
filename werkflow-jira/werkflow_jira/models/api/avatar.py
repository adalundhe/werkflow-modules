from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr


class Avatar(BaseModel):
    model_config = ConfigDict(extra="allow")

    fileName: StrictStr | None = None
    id: StrictStr | None = None
    isDeletable: StrictBool | None = None
    isSelected: StrictBool | None = None
    isSystemAvatar: StrictBool | None = None
    owner: StrictStr | None = None
    urls: dict[StrictStr, StrictStr] | None = None
