from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SupportCreateCaseRequest(BaseModel):
    subject: StrictStr
    communicationBody: StrictStr
    serviceCode: StrictStr | None = None
    severityCode: StrictStr | None = None
    categoryCode: StrictStr | None = None
    ccEmailAddresses: list[StrictStr] | None = None
    language: StrictStr | None = None
    issueType: StrictStr | None = None
    attachmentSetId: StrictStr | None = None
    uploadIds: list[StrictStr] | None = None
    dryRun: StrictBool | None = None
