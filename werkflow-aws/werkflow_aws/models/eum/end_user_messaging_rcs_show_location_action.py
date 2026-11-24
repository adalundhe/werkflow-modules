from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class EndUserMessagingRcsShowLocationAction(BaseModel):
    Text: StrictStr
    PostbackData: StrictStr
    Latitude: StrictFloat | StrictInt
    Longitude: StrictFloat | StrictInt
    Label: StrictStr | None = None
