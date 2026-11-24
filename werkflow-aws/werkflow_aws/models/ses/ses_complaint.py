from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESComplaint(BaseModel):
    ComplaintSubType: StrictStr | None = None
    ComplaintFeedbackType: StrictStr | None = None
