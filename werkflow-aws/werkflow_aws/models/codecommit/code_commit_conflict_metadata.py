from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .code_commit_file_modes import CodeCommitFileModes
from .code_commit_file_sizes import CodeCommitFileSizes
from .code_commit_is_binary_file import CodeCommitIsBinaryFile
from .code_commit_merge_operations import CodeCommitMergeOperations
from .code_commit_object_types import CodeCommitObjectTypes


class CodeCommitConflictMetadata(BaseModel):
    filePath: StrictStr | None = None
    fileSizes: CodeCommitFileSizes | None = None
    fileModes: CodeCommitFileModes | None = None
    objectTypes: CodeCommitObjectTypes | None = None
    numberOfConflicts: StrictInt | None = None
    isBinaryFile: CodeCommitIsBinaryFile | None = None
    contentConflict: StrictBool | None = None
    fileModeConflict: StrictBool | None = None
    objectTypeConflict: StrictBool | None = None
    mergeOperations: CodeCommitMergeOperations | None = None
