from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointDefaultButtonConfiguration(BaseModel):
    BackgroundColor: StrictStr | None = None
    BorderRadius: StrictInt | None = None
    ButtonAction: StrictStr | None = None
    Link: StrictStr | None = None
    Text: StrictStr | None = None
    TextColor: StrictStr | None = None
