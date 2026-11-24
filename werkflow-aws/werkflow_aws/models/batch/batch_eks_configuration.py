from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_eks_access_entry import BatchEksAccessEntry


class BatchEksConfiguration(BaseModel):
    eksClusterArn: StrictStr | None = None
    kubernetesNamespace: StrictStr | None = None
    accessEntry: BatchEksAccessEntry | None = None
