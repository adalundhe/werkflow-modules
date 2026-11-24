from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .macie_job_scope_term import MacieJobScopeTerm


class MacieJobScopingBlock(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    and_: list[MacieJobScopeTerm] | None = Field(default=None, alias='and')
