from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class MacieSearchResourcesSortCriteria(BaseModel):
    attributeName: Literal['ACCOUNT_ID', 'RESOURCE_NAME', 'S3_CLASSIFIABLE_OBJECT_COUNT', 'S3_CLASSIFIABLE_SIZE_IN_BYTES'] | None = None
    orderBy: Literal['ASC', 'DESC'] | None = None
