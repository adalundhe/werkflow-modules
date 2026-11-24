from __future__ import annotations
from pydantic import BaseModel
from .awss3_progress import AWSS3Progress


class AWSS3ProgressEvent(BaseModel):
    Details: AWSS3Progress | None = None
