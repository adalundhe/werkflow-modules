from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectCreateAttachedFileRequest(BaseModel):
    InstanceId: StrictStr
    FileUseCaseType: Literal['CONTACT_ANALYSIS', 'EMAIL_MESSAGE', 'EMAIL_MESSAGE_PLAIN_TEXT', 'EMAIL_MESSAGE_REDACTED', 'EMAIL_MESSAGE_PLAIN_TEXT_REDACTED', 'ATTACHMENT', 'VOICE_RECORDING', 'VOICEMAIL_RECORDING', 'VOICEMAIL_RECORDING_REDACTED', 'VOICEMAIL_ANALYSIS', 'VOICEMAIL_ANALYSIS_REDACTED']
    FileSourceUri: StrictStr
    AssociatedResourceArn: StrictStr
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
