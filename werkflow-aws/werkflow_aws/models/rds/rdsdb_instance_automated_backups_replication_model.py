from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBInstanceAutomatedBackupsReplicationModel(BaseModel):
    DBInstanceAutomatedBackupsArn: StrictStr | None = None
