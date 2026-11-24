from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_create_association_batch_request_entry import SSMCreateAssociationBatchRequestEntry


class SSMCreateAssociationBatchRequest(BaseModel):
    Entries: list[SSMCreateAssociationBatchRequestEntry]
    AssociationDispatchAssumeRole: StrictStr | None = None
