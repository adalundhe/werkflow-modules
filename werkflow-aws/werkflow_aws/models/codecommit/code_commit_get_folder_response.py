from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_file import CodeCommitFile
from .code_commit_folder import CodeCommitFolder
from .code_commit_sub_module import CodeCommitSubModule
from .code_commit_symbolic_link import CodeCommitSymbolicLink


class CodeCommitGetFolderResponse(BaseModel):
    commitId: StrictStr | None = None
    folderPath: StrictStr | None = None
    treeId: StrictStr | None = None
    subFolders: list[CodeCommitFolder] | None = None
    files: list[CodeCommitFile] | None = None
    symbolicLinks: list[CodeCommitSymbolicLink] | None = None
    subModules: list[CodeCommitSubModule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
