from __future__ import annotations
from pydantic import BaseModel
from .ses_bounce import SESBounce
from .ses_complaint import SESComplaint


class SESEventDetails(BaseModel):
    Bounce: SESBounce | None = None
    Complaint: SESComplaint | None = None
