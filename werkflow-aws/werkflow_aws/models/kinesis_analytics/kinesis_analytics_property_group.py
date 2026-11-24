from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsPropertyGroup(BaseModel):
    PropertyGroupId: StrictStr | None = None
    PropertyMap: dict[StrictStr, StrictStr] | None = None
