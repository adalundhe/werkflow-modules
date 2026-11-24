from __future__ import annotations
from pydantic import BaseModel
from .glue_catalog_target import GlueCatalogTarget
from .glue_delta_target import GlueDeltaTarget
from .glue_dynamo_db_target import GlueDynamoDBTarget
from .glue_hudi_target import GlueHudiTarget
from .glue_iceberg_target import GlueIcebergTarget
from .glue_jdbc_target import GlueJdbcTarget
from .glue_mongo_db_target import GlueMongoDBTarget
from .glue_s3_target import GlueS3Target


class GlueCrawlerTargets(BaseModel):
    S3Targets: list[GlueS3Target] | None = None
    JdbcTargets: list[GlueJdbcTarget] | None = None
    MongoDBTargets: list[GlueMongoDBTarget] | None = None
    DynamoDBTargets: list[GlueDynamoDBTarget] | None = None
    CatalogTargets: list[GlueCatalogTarget] | None = None
    DeltaTargets: list[GlueDeltaTarget] | None = None
    IcebergTargets: list[GlueIcebergTarget] | None = None
    HudiTargets: list[GlueHudiTarget] | None = None
