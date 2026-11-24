from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class FSxDeleteVolumeOpenZFSConfiguration(BaseModel):
    Options: list[Literal['DELETE_CHILD_VOLUMES_AND_SNAPSHOTS']] | None = None
