from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_review_details import SESReviewDetails


class SESAccountDetails(BaseModel):
    MailType: StrictStr | None = None
    WebsiteURL: StrictStr | None = None
    ContactLanguage: StrictStr | None = None
    UseCaseDescription: StrictStr | None = None
    AdditionalContactEmailAddresses: list[StrictStr] | None = None
    ReviewDetails: SESReviewDetails | None = None
