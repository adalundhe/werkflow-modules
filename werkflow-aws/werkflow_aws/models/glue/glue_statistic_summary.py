from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .glue_distribution_data import GlueDistributionData
from .glue_run_identifier import GlueRunIdentifier
from .glue_timestamped_inclusion_annotation import GlueTimestampedInclusionAnnotation


class GlueStatisticSummary(BaseModel):
    StatisticId: StrictStr | None = None
    ProfileId: StrictStr | None = None
    RunIdentifier: GlueRunIdentifier | None = None
    StatisticName: StrictStr | None = None
    DoubleValue: StrictFloat | StrictInt | None = None
    DistributionValue: GlueDistributionData | None = None
    EvaluationLevel: StrictStr | None = None
    ColumnsReferenced: list[StrictStr] | None = None
    ReferencedDatasets: list[StrictStr] | None = None
    StatisticProperties: dict[StrictStr, StrictStr] | None = None
    RecordedOn: datetime.datetime | StrictStr | None = None
    InclusionAnnotation: GlueTimestampedInclusionAnnotation | None = None
