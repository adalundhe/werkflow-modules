from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_accounting_database import SageMakerClusterAccountingDatabase


class SageMakerClusterOrchestratorSlurmConfig(BaseModel):
    SlurmConfigStrategy: StrictStr | None = None
    AccountingDatabase: SageMakerClusterAccountingDatabase | None = None
