from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_code_signing import IoTCodeSigning
from .io_t_file_location import IoTFileLocation


class IoTOTAUpdateFile(BaseModel):
    fileName: StrictStr | None = None
    fileType: StrictInt | None = None
    fileVersion: StrictStr | None = None
    fileLocation: IoTFileLocation | None = None
    codeSigning: IoTCodeSigning | None = None
    attributes: dict[StrictStr, StrictStr] | None = None
