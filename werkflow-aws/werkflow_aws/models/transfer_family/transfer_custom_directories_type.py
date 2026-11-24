from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferCustomDirectoriesType(BaseModel):
    FailedFilesDirectory: StrictStr | None = None
    MdnFilesDirectory: StrictStr | None = None
    PayloadFilesDirectory: StrictStr | None = None
    StatusFilesDirectory: StrictStr | None = None
    TemporaryFilesDirectory: StrictStr | None = None
