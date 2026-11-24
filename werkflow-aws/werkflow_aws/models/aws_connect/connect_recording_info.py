from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectRecordingInfo(BaseModel):
    StorageType: StrictStr | None = None
    Location: StrictStr | None = None
    MediaStreamType: StrictStr | None = None
    ParticipantType: StrictStr | None = None
    FragmentStartNumber: StrictStr | None = None
    FragmentStopNumber: StrictStr | None = None
    StartTimestamp: datetime.datetime | StrictStr | None = None
    StopTimestamp: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    DeletionReason: StrictStr | None = None
    UnprocessedTranscriptLocation: StrictStr | None = None
