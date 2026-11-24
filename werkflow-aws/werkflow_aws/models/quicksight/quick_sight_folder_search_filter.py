from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightFolderSearchFilter(BaseModel):
    Operator: Literal['StringEquals', 'StringLike'] | None = None
    Name: Literal['PARENT_FOLDER_ARN', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_VIEWER_OR_OWNER', 'FOLDER_NAME'] | None = None
    Value: StrictStr | None = None
