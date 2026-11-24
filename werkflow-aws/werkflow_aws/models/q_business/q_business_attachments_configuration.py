from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class QBusinessAttachmentsConfiguration(BaseModel):
    attachmentsControlMode: Literal['ENABLED', 'DISABLED']
