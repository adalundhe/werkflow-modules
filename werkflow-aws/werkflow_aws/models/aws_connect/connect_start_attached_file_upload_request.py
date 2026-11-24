from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_created_by_info import ConnectCreatedByInfo


class ConnectStartAttachedFileUploadRequest(BaseModel):
    InstanceId: StrictStr
    FileName: StrictStr
    FileSizeInBytes: StrictInt
    FileUseCaseType: Literal['CONTACT_ANALYSIS', 'EMAIL_MESSAGE', 'EMAIL_MESSAGE_PLAIN_TEXT', 'EMAIL_MESSAGE_REDACTED', 'EMAIL_MESSAGE_PLAIN_TEXT_REDACTED', 'ATTACHMENT', 'VOICE_RECORDING', 'VOICEMAIL_RECORDING', 'VOICEMAIL_RECORDING_REDACTED', 'VOICEMAIL_ANALYSIS', 'VOICEMAIL_ANALYSIS_REDACTED']
    AssociatedResourceArn: StrictStr
    ClientToken: StrictStr | None = None
    UrlExpiryInSeconds: StrictInt | None = None
    CreatedBy: ConnectCreatedByInfo | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
