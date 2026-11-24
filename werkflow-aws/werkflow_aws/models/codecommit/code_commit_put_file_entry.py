from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .code_commit_source_file_specifier import CodeCommitSourceFileSpecifier


class CodeCommitPutFileEntry(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    filePath: StrictStr
    fileMode: Literal['EXECUTABLE', 'NORMAL', 'SYMLINK'] | None = None
    fileContent: StrictBytes | BinaryIO | StrictStr | None = None
    sourceFile: CodeCommitSourceFileSpecifier | None = None
