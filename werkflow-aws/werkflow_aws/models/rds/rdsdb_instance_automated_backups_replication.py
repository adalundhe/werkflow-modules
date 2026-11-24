from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBInstanceAutomatedBackupsReplication(BaseModel):
    DBInstanceAutomatedBackupsArn: StrictStr | None = None
