from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_serverless_vector_options import OpenSearchServerlessVectorOptions


class OpenSearchServerlessCreateCollectionDetail(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
    description: StrictStr | None = None
    arn: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
    standbyReplicas: StrictStr | None = None
    deletionProtection: StrictStr | None = None
    vectorOptions: OpenSearchServerlessVectorOptions | None = None
    createdDate: StrictInt | None = None
    lastModifiedDate: StrictInt | None = None
    collectionGroupName: StrictStr | None = None
