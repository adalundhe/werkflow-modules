from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectListContactReferencesRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    ReferenceTypes: list[Literal['URL', 'ATTACHMENT', 'CONTACT_ANALYSIS', 'NUMBER', 'STRING', 'DATE', 'EMAIL', 'EMAIL_MESSAGE', 'EMAIL_MESSAGE_PLAIN_TEXT', 'EMAIL_MESSAGE_PLAIN_TEXT_REDACTED', 'EMAIL_MESSAGE_REDACTED', 'VOICEMAIL_RECORDING', 'VOICEMAIL_RECORDING_REDACTED', 'VOICEMAIL_ANALYSIS', 'VOICEMAIL_ANALYSIS_REDACTED']]
    NextToken: StrictStr | None = None
