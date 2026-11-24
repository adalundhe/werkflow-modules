from __future__ import annotations
from pydantic import BaseModel
from .memory_db_slot_migration import MemoryDBSlotMigration


class MemoryDBReshardingStatus(BaseModel):
    SlotMigration: MemoryDBSlotMigration | None = None
