from __future__ import annotations
from pydantic import BaseModel
from .code_commit_delete_file_entry import CodeCommitDeleteFileEntry
from .code_commit_replace_content_entry import CodeCommitReplaceContentEntry
from .code_commit_set_file_mode_entry import CodeCommitSetFileModeEntry


class CodeCommitConflictResolution(BaseModel):
    replaceContents: list[CodeCommitReplaceContentEntry] | None = None
    deleteFiles: list[CodeCommitDeleteFileEntry] | None = None
    setFileModes: list[CodeCommitSetFileModeEntry] | None = None
