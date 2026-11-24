from __future__ import annotations
from pydantic import BaseModel
from .ses_default_signing_scheme import SESDefaultSigningScheme
from .ses_smime_signing_scheme import SESSmimeSigningScheme


class SESSigningScheme(BaseModel):
    DefaultScheme: SESDefaultSigningScheme | None = None
    SmimeScheme: SESSmimeSigningScheme | None = None
