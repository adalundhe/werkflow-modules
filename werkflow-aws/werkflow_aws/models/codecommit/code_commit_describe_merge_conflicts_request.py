from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitDescribeMergeConflictsRequest(BaseModel):
    repositoryName: StrictStr
    destinationCommitSpecifier: StrictStr
    sourceCommitSpecifier: StrictStr
    mergeOption: Literal['FAST_FORWARD_MERGE', 'SQUASH_MERGE', 'THREE_WAY_MERGE']
    filePath: StrictStr
    maxMergeHunks: StrictInt | None = None
    conflictDetailLevel: Literal['FILE_LEVEL', 'LINE_LEVEL'] | None = None
    conflictResolutionStrategy: Literal['NONE', 'ACCEPT_SOURCE', 'ACCEPT_DESTINATION', 'AUTOMERGE'] | None = None
    nextToken: StrictStr | None = None
