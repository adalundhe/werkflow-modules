from __future__ import annotations
from pydantic import BaseModel
from .acm_dns_validation_challenge import ACMDnsValidationChallenge
from .acm_email_validation_challenge import ACMEmailValidationChallenge


class ACMValidationChallenge(BaseModel):
    EmailValidationChallenge: ACMEmailValidationChallenge | None = None
    DnsValidationChallenge: ACMDnsValidationChallenge | None = None
