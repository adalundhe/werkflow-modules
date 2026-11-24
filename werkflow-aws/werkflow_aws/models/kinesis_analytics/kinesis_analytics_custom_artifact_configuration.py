from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .kinesis_analytics_maven_reference import KinesisAnalyticsMavenReference
from .kinesis_analytics_s3_content_location import KinesisAnalyticsS3ContentLocation


class KinesisAnalyticsCustomArtifactConfiguration(BaseModel):
    ArtifactType: Literal['UDF', 'DEPENDENCY_JAR']
    S3ContentLocation: KinesisAnalyticsS3ContentLocation | None = None
    MavenReference: KinesisAnalyticsMavenReference | None = None
