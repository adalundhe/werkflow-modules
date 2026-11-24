from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectDisassociateInstanceStorageConfigRequest(BaseModel):
    InstanceId: StrictStr
    AssociationId: StrictStr
    ResourceType: Literal['CHAT_TRANSCRIPTS', 'CALL_RECORDINGS', 'SCHEDULED_REPORTS', 'MEDIA_STREAMS', 'CONTACT_TRACE_RECORDS', 'AGENT_EVENTS', 'REAL_TIME_CONTACT_ANALYSIS_SEGMENTS', 'ATTACHMENTS', 'CONTACT_EVALUATIONS', 'SCREEN_RECORDINGS', 'REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS', 'EMAIL_MESSAGES']
    ClientToken: StrictStr | None = None
