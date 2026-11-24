from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class SWFCloseStatusFilter(BaseModel):
    status: Literal['COMPLETED', 'FAILED', 'CANCELED', 'TERMINATED', 'CONTINUED_AS_NEW', 'TIMED_OUT']
