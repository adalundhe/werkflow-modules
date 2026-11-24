from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_maven_reference import KinesisAnalyticsMavenReference
from .kinesis_analytics_s3_content_location import KinesisAnalyticsS3ContentLocation


class KinesisAnalyticsCustomArtifactConfigurationDescription(BaseModel):
    ArtifactType: StrictStr | None = None
    S3ContentLocationDescription: KinesisAnalyticsS3ContentLocation | None = None
    MavenReferenceDescription: KinesisAnalyticsMavenReference | None = None
