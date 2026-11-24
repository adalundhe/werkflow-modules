from __future__ import annotations
from pydantic import BaseModel
from .ecr_delete_replication import ECRDeleteReplication
from .ecr_replication_destination import ECRReplicationDestination
from .ecr_repository_filter import ECRRepositoryFilter


class ECRReplicationRule(BaseModel):
    destinations: list[ECRReplicationDestination] | None = None
    repositoryFilters: list[ECRRepositoryFilter] | None = None
    deleteReplication: ECRDeleteReplication | None = None
