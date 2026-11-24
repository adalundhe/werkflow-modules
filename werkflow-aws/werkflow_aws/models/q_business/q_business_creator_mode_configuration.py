from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class QBusinessCreatorModeConfiguration(BaseModel):
    creatorModeControl: Literal['ENABLED', 'DISABLED']
