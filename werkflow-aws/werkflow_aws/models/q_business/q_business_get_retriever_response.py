from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_retriever_configuration import QBusinessRetrieverConfiguration


class QBusinessGetRetrieverResponse(BaseModel):
    applicationId: StrictStr | None = None
    retrieverId: StrictStr | None = None
    retrieverArn: StrictStr | None = None
    type: StrictStr | None = None
    status: StrictStr | None = None
    displayName: StrictStr | None = None
    configuration: QBusinessRetrieverConfiguration | None = None
    roleArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
