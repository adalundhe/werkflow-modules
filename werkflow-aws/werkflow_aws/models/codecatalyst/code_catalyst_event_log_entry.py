from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_catalyst_event_payload import CodeCatalystEventPayload
from .code_catalyst_project_information import CodeCatalystProjectInformation
from .code_catalyst_user_identity import CodeCatalystUserIdentity


class CodeCatalystEventLogEntry(BaseModel):
    id: StrictStr | None = None
    eventName: StrictStr | None = None
    eventType: StrictStr | None = None
    eventCategory: StrictStr | None = None
    eventSource: StrictStr | None = None
    eventTime: datetime.datetime | StrictStr | None = None
    operationType: StrictStr | None = None
    userIdentity: CodeCatalystUserIdentity | None = None
    projectInformation: CodeCatalystProjectInformation | None = None
    requestId: StrictStr | None = None
    requestPayload: CodeCatalystEventPayload | None = None
    responsePayload: CodeCatalystEventPayload | None = None
    errorCode: StrictStr | None = None
    sourceIpAddress: StrictStr | None = None
    userAgent: StrictStr | None = None
