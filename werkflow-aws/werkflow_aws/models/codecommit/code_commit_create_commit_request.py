from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .code_commit_delete_file_entry import CodeCommitDeleteFileEntry
from .code_commit_put_file_entry import CodeCommitPutFileEntry
from .code_commit_set_file_mode_entry import CodeCommitSetFileModeEntry


class CodeCommitCreateCommitRequest(BaseModel):
    repositoryName: StrictStr
    branchName: StrictStr
    parentCommitId: StrictStr | None = None
    authorName: StrictStr | None = None
    email: StrictStr | None = None
    commitMessage: StrictStr | None = None
    keepEmptyFolders: StrictBool | None = None
    putFiles: list[CodeCommitPutFileEntry] | None = None
    deleteFiles: list[CodeCommitDeleteFileEntry] | None = None
    setFileModes: list[CodeCommitSetFileModeEntry] | None = None
