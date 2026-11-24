from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESSuppressedDestinationAttributes(BaseModel):
    MessageId: StrictStr | None = None
    FeedbackId: StrictStr | None = None
