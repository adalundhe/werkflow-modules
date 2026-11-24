from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .awss3_delete_marker_replication import AWSS3DeleteMarkerReplication
from .awss3_destination import AWSS3Destination
from .awss3_existing_object_replication import AWSS3ExistingObjectReplication
from .awss3_replication_rule_filter import AWSS3ReplicationRuleFilter
from .awss3_source_selection_criteria import AWSS3SourceSelectionCriteria


class AWSS3ReplicationRule(BaseModel):
    ID: StrictStr | None = None
    Priority: StrictInt | None = None
    Prefix: StrictStr | None = None
    Filter: AWSS3ReplicationRuleFilter | None = None
    Status: StrictStr | None = None
    SourceSelectionCriteria: AWSS3SourceSelectionCriteria | None = None
    ExistingObjectReplication: AWSS3ExistingObjectReplication | None = None
    Destination: AWSS3Destination | None = None
    DeleteMarkerReplication: AWSS3DeleteMarkerReplication | None = None
