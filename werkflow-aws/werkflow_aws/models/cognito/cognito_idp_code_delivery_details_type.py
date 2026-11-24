from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPCodeDeliveryDetailsType(BaseModel):
    Destination: StrictStr | None = None
    DeliveryMedium: StrictStr | None = None
    AttributeName: StrictStr | None = None
