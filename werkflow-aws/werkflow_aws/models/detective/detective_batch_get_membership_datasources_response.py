from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .detective_membership_datasources import DetectiveMembershipDatasources
from .detective_unprocessed_graph import DetectiveUnprocessedGraph


class DetectiveBatchGetMembershipDatasourcesResponse(BaseModel):
    MembershipDatasources: list[DetectiveMembershipDatasources] | None = None
    UnprocessedGraphs: list[DetectiveUnprocessedGraph] | None = None
    ResponseMetadata: dict[str, Any] | None = None
