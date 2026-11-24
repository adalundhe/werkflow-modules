from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class DirectoryServiceDirectorySizeUpdateSettings(BaseModel):
    DirectorySize: Literal['Small', 'Large'] | None = None
