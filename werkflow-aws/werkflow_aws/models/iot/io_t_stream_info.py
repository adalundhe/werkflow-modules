from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_stream_file import IoTStreamFile


class IoTStreamInfo(BaseModel):
    streamId: StrictStr | None = None
    streamArn: StrictStr | None = None
    streamVersion: StrictInt | None = None
    description: StrictStr | None = None
    files: list[IoTStreamFile] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    roleArn: StrictStr | None = None
