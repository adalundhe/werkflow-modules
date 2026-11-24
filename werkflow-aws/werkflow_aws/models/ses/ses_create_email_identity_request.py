from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_dkim_signing_attributes import SESDkimSigningAttributes
from .ses_tag import SESTag


class SESCreateEmailIdentityRequest(BaseModel):
    EmailIdentity: StrictStr
    Tags: list[SESTag] | None = None
    DkimSigningAttributes: SESDkimSigningAttributes | None = None
    ConfigurationSetName: StrictStr | None = None
