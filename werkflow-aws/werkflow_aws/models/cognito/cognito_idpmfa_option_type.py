from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPMFAOptionType(BaseModel):
    DeliveryMedium: StrictStr | None = None
    AttributeName: StrictStr | None = None
