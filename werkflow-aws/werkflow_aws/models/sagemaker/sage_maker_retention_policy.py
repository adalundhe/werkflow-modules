from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class SageMakerRetentionPolicy(BaseModel):
    HomeEfsFileSystem: Literal['Retain', 'Delete'] | None = None
