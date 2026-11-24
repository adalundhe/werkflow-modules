from __future__ import annotations
from pydantic import BaseModel
from .elasti_cache_slot_migration import ElastiCacheSlotMigration


class ElastiCacheReshardingStatus(BaseModel):
    SlotMigration: ElastiCacheSlotMigration | None = None
