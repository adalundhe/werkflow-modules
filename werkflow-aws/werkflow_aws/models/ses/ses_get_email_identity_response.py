from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ses_dkim_attributes import SESDkimAttributes
from .ses_mail_from_attributes import SESMailFromAttributes
from .ses_tag import SESTag
from .ses_verification_info import SESVerificationInfo


class SESGetEmailIdentityResponse(BaseModel):
    IdentityType: StrictStr | None = None
    FeedbackForwardingStatus: StrictBool | None = None
    VerifiedForSendingStatus: StrictBool | None = None
    DkimAttributes: SESDkimAttributes | None = None
    MailFromAttributes: SESMailFromAttributes | None = None
    Policies: dict[StrictStr, StrictStr] | None = None
    Tags: list[SESTag] | None = None
    ConfigurationSetName: StrictStr | None = None
    VerificationStatus: StrictStr | None = None
    VerificationInfo: SESVerificationInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
