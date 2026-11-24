from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .amplify_branch import AmplifyBranch


class AmplifyListBranchesResponse(BaseModel):
    branches: list[AmplifyBranch] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
