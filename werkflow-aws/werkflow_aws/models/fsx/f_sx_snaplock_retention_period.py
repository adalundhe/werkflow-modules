from __future__ import annotations
from pydantic import BaseModel
from .f_sx_retention_period import FSxRetentionPeriod


class FSxSnaplockRetentionPeriod(BaseModel):
    DefaultRetention: FSxRetentionPeriod | None = None
    MinimumRetention: FSxRetentionPeriod | None = None
    MaximumRetention: FSxRetentionPeriod | None = None
