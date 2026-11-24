from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class CodeCommitPutFileRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    repositoryName: StrictStr
    branchName: StrictStr
    fileContent: StrictBytes | BinaryIO | StrictStr
    filePath: StrictStr
    fileMode: Literal['EXECUTABLE', 'NORMAL', 'SYMLINK'] | None = None
    parentCommitId: StrictStr | None = None
    commitMessage: StrictStr | None = None
    name: StrictStr | None = None
    email: StrictStr | None = None
