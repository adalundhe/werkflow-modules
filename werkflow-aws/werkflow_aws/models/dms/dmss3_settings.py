from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSS3Settings(BaseModel):
    ServiceAccessRoleArn: StrictStr | None = None
    ExternalTableDefinition: StrictStr | None = None
    CsvRowDelimiter: StrictStr | None = None
    CsvDelimiter: StrictStr | None = None
    BucketFolder: StrictStr | None = None
    BucketName: StrictStr | None = None
    CompressionType: StrictStr | None = None
    EncryptionMode: StrictStr | None = None
    ServerSideEncryptionKmsKeyId: StrictStr | None = None
    DataFormat: StrictStr | None = None
    EncodingType: StrictStr | None = None
    DictPageSizeLimit: StrictInt | None = None
    RowGroupLength: StrictInt | None = None
    DataPageSize: StrictInt | None = None
    ParquetVersion: StrictStr | None = None
    EnableStatistics: StrictBool | None = None
    IncludeOpForFullLoad: StrictBool | None = None
    CdcInsertsOnly: StrictBool | None = None
    TimestampColumnName: StrictStr | None = None
    ParquetTimestampInMillisecond: StrictBool | None = None
    CdcInsertsAndUpdates: StrictBool | None = None
    DatePartitionEnabled: StrictBool | None = None
    DatePartitionSequence: StrictStr | None = None
    DatePartitionDelimiter: StrictStr | None = None
    UseCsvNoSupValue: StrictBool | None = None
    CsvNoSupValue: StrictStr | None = None
    PreserveTransactions: StrictBool | None = None
    CdcPath: StrictStr | None = None
    UseTaskStartTimeForFullLoadTimestamp: StrictBool | None = None
    CannedAclForObjects: StrictStr | None = None
    AddColumnName: StrictBool | None = None
    CdcMaxBatchInterval: StrictInt | None = None
    CdcMinFileSize: StrictInt | None = None
    CsvNullValue: StrictStr | None = None
    IgnoreHeaderRows: StrictInt | None = None
    MaxFileSize: StrictInt | None = None
    Rfc4180: StrictBool | None = None
    DatePartitionTimezone: StrictStr | None = None
    AddTrailingPaddingCharacter: StrictBool | None = None
    ExpectedBucketOwner: StrictStr | None = None
    GlueCatalogGeneration: StrictBool | None = None
