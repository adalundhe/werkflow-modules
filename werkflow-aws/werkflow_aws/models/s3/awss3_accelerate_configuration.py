from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AWSS3AccelerateConfiguration(BaseModel):
    Status: Literal['Enabled', 'Suspended'] | None = None
