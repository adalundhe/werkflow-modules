from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_amazon_open_search_serverless_destination_update import FirehoseAmazonOpenSearchServerlessDestinationUpdate
from .firehose_amazonopensearchservice_destination_update import FirehoseAmazonopensearchserviceDestinationUpdate
from .firehose_elasticsearch_destination_update import FirehoseElasticsearchDestinationUpdate
from .firehose_extended_s3_destination_update import FirehoseExtendedS3DestinationUpdate
from .firehose_http_endpoint_destination_update import FirehoseHttpEndpointDestinationUpdate
from .firehose_iceberg_destination_update import FirehoseIcebergDestinationUpdate
from .firehose_redshift_destination_update import FirehoseRedshiftDestinationUpdate
from .firehose_s3_destination_update import FirehoseS3DestinationUpdate
from .firehose_snowflake_destination_update import FirehoseSnowflakeDestinationUpdate
from .firehose_splunk_destination_update import FirehoseSplunkDestinationUpdate


class FirehoseUpdateDestinationRequest(BaseModel):
    DeliveryStreamName: StrictStr
    CurrentDeliveryStreamVersionId: StrictStr
    DestinationId: StrictStr
    S3DestinationUpdate: FirehoseS3DestinationUpdate | None = None
    ExtendedS3DestinationUpdate: FirehoseExtendedS3DestinationUpdate | None = None
    RedshiftDestinationUpdate: FirehoseRedshiftDestinationUpdate | None = None
    ElasticsearchDestinationUpdate: FirehoseElasticsearchDestinationUpdate | None = None
    AmazonopensearchserviceDestinationUpdate: FirehoseAmazonopensearchserviceDestinationUpdate | None = None
    SplunkDestinationUpdate: FirehoseSplunkDestinationUpdate | None = None
    HttpEndpointDestinationUpdate: FirehoseHttpEndpointDestinationUpdate | None = None
    AmazonOpenSearchServerlessDestinationUpdate: FirehoseAmazonOpenSearchServerlessDestinationUpdate | None = None
    SnowflakeDestinationUpdate: FirehoseSnowflakeDestinationUpdate | None = None
    IcebergDestinationUpdate: FirehoseIcebergDestinationUpdate | None = None
