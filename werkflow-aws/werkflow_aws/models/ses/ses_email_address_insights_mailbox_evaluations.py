from __future__ import annotations
from pydantic import BaseModel
from .ses_email_address_insights_verdict import SESEmailAddressInsightsVerdict


class SESEmailAddressInsightsMailboxEvaluations(BaseModel):
    HasValidSyntax: SESEmailAddressInsightsVerdict | None = None
    HasValidDnsRecords: SESEmailAddressInsightsVerdict | None = None
    MailboxExists: SESEmailAddressInsightsVerdict | None = None
    IsRoleAddress: SESEmailAddressInsightsVerdict | None = None
    IsDisposable: SESEmailAddressInsightsVerdict | None = None
    IsRandomInput: SESEmailAddressInsightsVerdict | None = None
