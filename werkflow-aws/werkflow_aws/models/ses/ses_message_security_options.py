from __future__ import annotations
from pydantic import BaseModel
from .ses_signing_scheme import SESSigningScheme


class SESMessageSecurityOptions(BaseModel):
    SigningScheme: SESSigningScheme | None = None
