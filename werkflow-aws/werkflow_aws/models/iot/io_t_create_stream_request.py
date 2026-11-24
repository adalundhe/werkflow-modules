from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_stream_file import IoTStreamFile
from .io_t_tag import IoTTag


class IoTCreateStreamRequest(BaseModel):
    streamId: StrictStr
    files: list[IoTStreamFile]
    roleArn: StrictStr
    description: StrictStr | None = None
    tags: list[IoTTag] | None = None
