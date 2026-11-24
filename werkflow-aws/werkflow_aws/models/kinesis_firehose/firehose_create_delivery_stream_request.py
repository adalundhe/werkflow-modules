from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .firehose_amazon_open_search_serverless_destination_configuration import FirehoseAmazonOpenSearchServerlessDestinationConfiguration
from .firehose_amazonopensearchservice_destination_configuration import FirehoseAmazonopensearchserviceDestinationConfiguration
from .firehose_database_source_configuration import FirehoseDatabaseSourceConfiguration
from .firehose_delivery_stream_encryption_configuration_input import FirehoseDeliveryStreamEncryptionConfigurationInput
from .firehose_direct_put_source_configuration import FirehoseDirectPutSourceConfiguration
from .firehose_elasticsearch_destination_configuration import FirehoseElasticsearchDestinationConfiguration
from .firehose_extended_s3_destination_configuration import FirehoseExtendedS3DestinationConfiguration
from .firehose_http_endpoint_destination_configuration import FirehoseHttpEndpointDestinationConfiguration
from .firehose_iceberg_destination_configuration import FirehoseIcebergDestinationConfiguration
from .firehose_kinesis_stream_source_configuration import FirehoseKinesisStreamSourceConfiguration
from .firehose_msk_source_configuration import FirehoseMSKSourceConfiguration
from .firehose_redshift_destination_configuration import FirehoseRedshiftDestinationConfiguration
from .firehose_s3_destination_configuration import FirehoseS3DestinationConfiguration
from .firehose_snowflake_destination_configuration import FirehoseSnowflakeDestinationConfiguration
from .firehose_splunk_destination_configuration import FirehoseSplunkDestinationConfiguration
from .firehose_tag import FirehoseTag


class FirehoseCreateDeliveryStreamRequest(BaseModel):
    DeliveryStreamName: StrictStr
    DeliveryStreamType: Literal['DirectPut', 'KinesisStreamAsSource', 'MSKAsSource', 'DatabaseAsSource'] | None = None
    DirectPutSourceConfiguration: FirehoseDirectPutSourceConfiguration | None = None
    KinesisStreamSourceConfiguration: FirehoseKinesisStreamSourceConfiguration | None = None
    DeliveryStreamEncryptionConfigurationInput: FirehoseDeliveryStreamEncryptionConfigurationInput | None = None
    S3DestinationConfiguration: FirehoseS3DestinationConfiguration | None = None
    ExtendedS3DestinationConfiguration: FirehoseExtendedS3DestinationConfiguration | None = None
    RedshiftDestinationConfiguration: FirehoseRedshiftDestinationConfiguration | None = None
    ElasticsearchDestinationConfiguration: FirehoseElasticsearchDestinationConfiguration | None = None
    AmazonopensearchserviceDestinationConfiguration: FirehoseAmazonopensearchserviceDestinationConfiguration | None = None
    SplunkDestinationConfiguration: FirehoseSplunkDestinationConfiguration | None = None
    HttpEndpointDestinationConfiguration: FirehoseHttpEndpointDestinationConfiguration | None = None
    Tags: list[FirehoseTag] | None = None
    AmazonOpenSearchServerlessDestinationConfiguration: FirehoseAmazonOpenSearchServerlessDestinationConfiguration | None = None
    MSKSourceConfiguration: FirehoseMSKSourceConfiguration | None = None
    SnowflakeDestinationConfiguration: FirehoseSnowflakeDestinationConfiguration | None = None
    IcebergDestinationConfiguration: FirehoseIcebergDestinationConfiguration | None = None
    DatabaseSourceConfiguration: FirehoseDatabaseSourceConfiguration | None = None
