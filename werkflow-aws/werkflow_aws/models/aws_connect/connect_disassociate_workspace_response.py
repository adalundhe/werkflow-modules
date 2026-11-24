from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_failed_batch_association_summary import ConnectFailedBatchAssociationSummary
from .connect_successful_batch_association_summary import ConnectSuccessfulBatchAssociationSummary


class ConnectDisassociateWorkspaceResponse(BaseModel):
    SuccessfulList: list[ConnectSuccessfulBatchAssociationSummary] | None = None
    FailedList: list[ConnectFailedBatchAssociationSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
