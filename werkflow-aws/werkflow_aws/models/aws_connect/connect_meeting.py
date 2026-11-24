from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_media_placement import ConnectMediaPlacement
from .connect_meeting_features_configuration import ConnectMeetingFeaturesConfiguration


class ConnectMeeting(BaseModel):
    MediaRegion: StrictStr | None = None
    MediaPlacement: ConnectMediaPlacement | None = None
    MeetingFeatures: ConnectMeetingFeaturesConfiguration | None = None
    MeetingId: StrictStr | None = None
