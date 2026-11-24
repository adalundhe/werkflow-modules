from __future__ import annotations
from pydantic import BaseModel
from .ses_email_address_insights_mailbox_evaluations import SESEmailAddressInsightsMailboxEvaluations
from .ses_email_address_insights_verdict import SESEmailAddressInsightsVerdict


class SESMailboxValidation(BaseModel):
    IsValid: SESEmailAddressInsightsVerdict | None = None
    Evaluations: SESEmailAddressInsightsMailboxEvaluations | None = None
