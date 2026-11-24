from __future__ import annotations
from pydantic import BaseModel
from .connect_attachment_reference import ConnectAttachmentReference
from .connect_contact_analysis_reference import ConnectContactAnalysisReference
from .connect_date_reference import ConnectDateReference
from .connect_email_message_reference import ConnectEmailMessageReference
from .connect_email_reference import ConnectEmailReference
from .connect_number_reference import ConnectNumberReference
from .connect_string_reference import ConnectStringReference
from .connect_url_reference import ConnectUrlReference
from .connect_voicemail_analysis_reference import ConnectVoicemailAnalysisReference
from .connect_voicemail_recording_reference import ConnectVoicemailRecordingReference


class ConnectReferenceSummary(BaseModel):
    Url: ConnectUrlReference | None = None
    Attachment: ConnectAttachmentReference | None = None
    EmailMessage: ConnectEmailMessageReference | None = None
    EmailMessageRedacted: ConnectEmailMessageReference | None = None
    EmailMessagePlainText: ConnectEmailMessageReference | None = None
    EmailMessagePlainTextRedacted: ConnectEmailMessageReference | None = None
    String: ConnectStringReference | None = None
    Number: ConnectNumberReference | None = None
    Date: ConnectDateReference | None = None
    Email: ConnectEmailReference | None = None
    ContactAnalysis: ConnectContactAnalysisReference | None = None
    VoicemailRecording: ConnectVoicemailRecordingReference | None = None
    VoicemailRecordingRedacted: ConnectVoicemailRecordingReference | None = None
    VoicemailAnalysis: ConnectVoicemailAnalysisReference | None = None
    VoicemailAnalysisRedacted: ConnectVoicemailAnalysisReference | None = None
