from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .amplify_branch import AmplifyBranch


class AmplifyCreateBranchResponse(BaseModel):
    branch: AmplifyBranch | None = None
    ResponseMetadata: dict[str, Any] | None = None
