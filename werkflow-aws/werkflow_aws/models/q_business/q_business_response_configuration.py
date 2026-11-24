from __future__ import annotations
from pydantic import BaseModel
from .q_business_instruction_collection import QBusinessInstructionCollection


class QBusinessResponseConfiguration(BaseModel):
    instructionCollection: QBusinessInstructionCollection | None = None
