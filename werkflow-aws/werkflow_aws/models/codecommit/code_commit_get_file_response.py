from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr


class CodeCommitGetFileResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    commitId: StrictStr | None = None
    blobId: StrictStr | None = None
    filePath: StrictStr | None = None
    fileMode: StrictStr | None = None
    fileSize: StrictInt | None = None
    fileContent: StrictBytes | Any | None = None
    ResponseMetadata: dict[str, Any] | None = None
