from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SupportAddCommunicationToCaseRequest(BaseModel):
    communicationBody: StrictStr
    caseId: StrictStr | None = None
    ccEmailAddresses: list[StrictStr] | None = None
    attachmentSetId: StrictStr | None = None
    uploadIds: list[StrictStr] | None = None
    dryRun: StrictBool | None = None
