from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_raw_email import PinpointRawEmail
from .pinpoint_simple_email import PinpointSimpleEmail


class PinpointEmailMessage(BaseModel):
    Body: StrictStr | None = None
    FeedbackForwardingAddress: StrictStr | None = None
    FromAddress: StrictStr | None = None
    RawEmail: PinpointRawEmail | None = None
    ReplyToAddresses: list[StrictStr] | None = None
    SimpleEmail: PinpointSimpleEmail | None = None
    Substitutions: dict[StrictStr, list[StrictStr]] | None = None
