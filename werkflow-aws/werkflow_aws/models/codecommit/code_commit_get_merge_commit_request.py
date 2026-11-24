from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeCommitGetMergeCommitRequest(BaseModel):
    repositoryName: StrictStr
    sourceCommitSpecifier: StrictStr
    destinationCommitSpecifier: StrictStr
    conflictDetailLevel: Literal['FILE_LEVEL', 'LINE_LEVEL'] | None = None
    conflictResolutionStrategy: Literal['NONE', 'ACCEPT_SOURCE', 'ACCEPT_DESTINATION', 'AUTOMERGE'] | None = None
