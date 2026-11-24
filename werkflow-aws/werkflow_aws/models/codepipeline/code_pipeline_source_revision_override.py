from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineSourceRevisionOverride(BaseModel):
    actionName: StrictStr
    revisionType: Literal['COMMIT_ID', 'IMAGE_DIGEST', 'S3_OBJECT_VERSION_ID', 'S3_OBJECT_KEY']
    revisionValue: StrictStr
