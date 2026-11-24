from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_dkim_signing_attributes import SESDkimSigningAttributes


class SESPutEmailIdentityDkimSigningAttributesRequest(BaseModel):
    EmailIdentity: StrictStr
    SigningAttributesOrigin: StrictStr
    SigningAttributes: SESDkimSigningAttributes | None = None
