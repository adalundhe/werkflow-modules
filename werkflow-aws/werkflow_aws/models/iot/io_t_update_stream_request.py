from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_stream_file import IoTStreamFile


class IoTUpdateStreamRequest(BaseModel):
    streamId: StrictStr
    description: StrictStr | None = None
    files: list[IoTStreamFile] | None = None
    roleArn: StrictStr | None = None
