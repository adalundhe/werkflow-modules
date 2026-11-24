from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class LexAudioFillerSettings(BaseModel):
    enabled: StrictBool | None = None
    audioType: StrictStr | None = None
    startDelayInMilliseconds: StrictInt | None = None
    minimumPlayDurationInMilliseconds: StrictInt | None = None
    responseDeliveryDelayInMilliseconds: StrictInt | None = None
