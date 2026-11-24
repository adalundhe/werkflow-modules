from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class MacieListJobsSortCriteria(BaseModel):
    attributeName: Literal['createdAt', 'jobStatus', 'name', 'jobType'] | None = None
    orderBy: Literal['ASC', 'DESC'] | None = None
