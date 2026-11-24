from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO, Callable
from boto3.s3.transfer import TransferConfig
from botocore.paginate import Paginator


class s3Client(ABC):

    @abstractmethod
    def list_buckets(
        self,
        *,
        MaxBuckets: int | None = None,
        ContinuationToken: str | None = None,
        Prefix: str | None = None,
        BucketRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_bucket(
        self,
        *,
        Bucket: str,
        ACL: str | None = None,
        CreateBucketConfiguration: dict[str, Any] | None = None,
        GrantFullControl: str | None = None,
        GrantRead: str | None = None,
        GrantReadACP: str | None = None,
        GrantWrite: str | None = None,
        GrantWriteACP: str | None = None,
        ObjectLockEnabledForBucket: bool | None = None,
        ObjectOwnership: str | None = None,
        BucketNamespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def head_bucket(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_objects_v2(
        self,
        *,
        Bucket: str,
        Delimiter: str | None = None,
        EncodingType: str | None = None,
        MaxKeys: int | None = None,
        Prefix: str | None = None,
        ContinuationToken: str | None = None,
        FetchOwner: bool | None = None,
        StartAfter: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
        OptionalObjectAttributes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def head_object(
        self,
        *,
        Bucket: str,
        Key: str,
        IfMatch: str | None = None,
        IfModifiedSince: datetime.datetime | str | None = None,
        IfNoneMatch: str | None = None,
        IfUnmodifiedSince: datetime.datetime | str | None = None,
        Range: str | None = None,
        ResponseCacheControl: str | None = None,
        ResponseContentDisposition: str | None = None,
        ResponseContentEncoding: str | None = None,
        ResponseContentLanguage: str | None = None,
        ResponseContentType: str | None = None,
        ResponseExpires: datetime.datetime | str | None = None,
        VersionId: str | None = None,
        SSECustomerAlgorithm: str | None = None,
        SSECustomerKey: str | None = None,
        SSECustomerKeyMD5: str | None = None,
        RequestPayer: str | None = None,
        PartNumber: int | None = None,
        ExpectedBucketOwner: str | None = None,
        ChecksumMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_object(
        self,
        *,
        Bucket: str,
        Key: str,
        IfMatch: str | None = None,
        IfModifiedSince: datetime.datetime | str | None = None,
        IfNoneMatch: str | None = None,
        IfUnmodifiedSince: datetime.datetime | str | None = None,
        Range: str | None = None,
        ResponseCacheControl: str | None = None,
        ResponseContentDisposition: str | None = None,
        ResponseContentEncoding: str | None = None,
        ResponseContentLanguage: str | None = None,
        ResponseContentType: str | None = None,
        ResponseExpires: datetime.datetime | str | None = None,
        VersionId: str | None = None,
        SSECustomerAlgorithm: str | None = None,
        SSECustomerKey: str | None = None,
        SSECustomerKeyMD5: str | None = None,
        RequestPayer: str | None = None,
        PartNumber: int | None = None,
        ExpectedBucketOwner: str | None = None,
        ChecksumMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_object(
        self,
        *,
        Bucket: str,
        Key: str,
        ACL: str | None = None,
        Body: bytes | BinaryIO | str | None = None,
        CacheControl: str | None = None,
        ContentDisposition: str | None = None,
        ContentEncoding: str | None = None,
        ContentLanguage: str | None = None,
        ContentLength: int | None = None,
        ContentMD5: str | None = None,
        ContentType: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ChecksumCRC32: str | None = None,
        ChecksumCRC32C: str | None = None,
        ChecksumCRC64NVME: str | None = None,
        ChecksumSHA1: str | None = None,
        ChecksumSHA256: str | None = None,
        ChecksumSHA512: str | None = None,
        ChecksumMD5: str | None = None,
        ChecksumXXHASH64: str | None = None,
        ChecksumXXHASH3: str | None = None,
        ChecksumXXHASH128: str | None = None,
        Expires: datetime.datetime | str | None = None,
        IfMatch: str | None = None,
        IfNoneMatch: str | None = None,
        GrantFullControl: str | None = None,
        GrantRead: str | None = None,
        GrantReadACP: str | None = None,
        GrantWriteACP: str | None = None,
        WriteOffsetBytes: int | None = None,
        Metadata: dict[str, str] | None = None,
        ServerSideEncryption: str | None = None,
        StorageClass: str | None = None,
        WebsiteRedirectLocation: str | None = None,
        SSECustomerAlgorithm: str | None = None,
        SSECustomerKey: str | None = None,
        SSECustomerKeyMD5: str | None = None,
        SSEKMSKeyId: str | None = None,
        SSEKMSEncryptionContext: str | None = None,
        BucketKeyEnabled: bool | None = None,
        RequestPayer: str | None = None,
        Tagging: str | None = None,
        ObjectLockMode: str | None = None,
        ObjectLockRetainUntilDate: datetime.datetime | str | None = None,
        ObjectLockLegalHoldStatus: str | None = None,
        ObjectLockEventHold: str | None = None,
        ObjectLockEventHoldDurationDays: int | None = None,
        ObjectLockEventHoldDurationYears: int | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_object(
        self,
        *,
        Bucket: str,
        Key: str,
        MFA: str | None = None,
        VersionId: str | None = None,
        RequestPayer: str | None = None,
        BypassGovernanceRetention: bool | None = None,
        ExpectedBucketOwner: str | None = None,
        IfMatch: str | None = None,
        IfMatchLastModifiedTime: datetime.datetime | str | None = None,
        IfMatchSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_objects(
        self,
        *,
        Bucket: str,
        Delete: dict[str, Any],
        MFA: str | None = None,
        RequestPayer: str | None = None,
        BypassGovernanceRetention: bool | None = None,
        ExpectedBucketOwner: str | None = None,
        ChecksumAlgorithm: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_multipart_uploads(
        self,
        *,
        Bucket: str,
        Delimiter: str | None = None,
        EncodingType: str | None = None,
        KeyMarker: str | None = None,
        MaxUploads: int | None = None,
        Prefix: str | None = None,
        UploadIdMarker: str | None = None,
        ExpectedBucketOwner: str | None = None,
        RequestPayer: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_parts(
        self,
        *,
        Bucket: str,
        Key: str,
        UploadId: str,
        MaxParts: int | None = None,
        PartNumberMarker: int | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
        SSECustomerAlgorithm: str | None = None,
        SSECustomerKey: str | None = None,
        SSECustomerKeyMD5: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def complete_multipart_upload(
        self,
        *,
        Bucket: str,
        Key: str,
        UploadId: str,
        MultipartUpload: dict[str, Any] | None = None,
        ChecksumCRC32: str | None = None,
        ChecksumCRC32C: str | None = None,
        ChecksumCRC64NVME: str | None = None,
        ChecksumSHA1: str | None = None,
        ChecksumSHA256: str | None = None,
        ChecksumSHA512: str | None = None,
        ChecksumMD5: str | None = None,
        ChecksumXXHASH64: str | None = None,
        ChecksumXXHASH3: str | None = None,
        ChecksumXXHASH128: str | None = None,
        ChecksumType: str | None = None,
        MpuObjectSize: int | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
        IfMatch: str | None = None,
        IfNoneMatch: str | None = None,
        SSECustomerAlgorithm: str | None = None,
        SSECustomerKey: str | None = None,
        SSECustomerKeyMD5: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def abort_multipart_upload(
        self,
        *,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
        IfMatchInitiatedTime: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_multipart_upload(
        self,
        *,
        Bucket: str,
        Key: str,
        ACL: str | None = None,
        CacheControl: str | None = None,
        ContentDisposition: str | None = None,
        ContentEncoding: str | None = None,
        ContentLanguage: str | None = None,
        ContentType: str | None = None,
        Expires: datetime.datetime | str | None = None,
        GrantFullControl: str | None = None,
        GrantRead: str | None = None,
        GrantReadACP: str | None = None,
        GrantWriteACP: str | None = None,
        Metadata: dict[str, str] | None = None,
        ServerSideEncryption: str | None = None,
        StorageClass: str | None = None,
        WebsiteRedirectLocation: str | None = None,
        SSECustomerAlgorithm: str | None = None,
        SSECustomerKey: str | None = None,
        SSECustomerKeyMD5: str | None = None,
        SSEKMSKeyId: str | None = None,
        SSEKMSEncryptionContext: str | None = None,
        BucketKeyEnabled: bool | None = None,
        RequestPayer: str | None = None,
        Tagging: str | None = None,
        ObjectLockMode: str | None = None,
        ObjectLockRetainUntilDate: datetime.datetime | str | None = None,
        ObjectLockLegalHoldStatus: str | None = None,
        ObjectLockEventHold: str | None = None,
        ObjectLockEventHoldDurationDays: int | None = None,
        ObjectLockEventHoldDurationYears: int | None = None,
        ExpectedBucketOwner: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ChecksumType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def upload_part(
        self,
        *,
        Bucket: str,
        Key: str,
        PartNumber: int,
        UploadId: str,
        Body: bytes | BinaryIO | str | None = None,
        ContentLength: int | None = None,
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ChecksumCRC32: str | None = None,
        ChecksumCRC32C: str | None = None,
        ChecksumCRC64NVME: str | None = None,
        ChecksumSHA1: str | None = None,
        ChecksumSHA256: str | None = None,
        ChecksumSHA512: str | None = None,
        ChecksumMD5: str | None = None,
        ChecksumXXHASH64: str | None = None,
        ChecksumXXHASH3: str | None = None,
        ChecksumXXHASH128: str | None = None,
        SSECustomerAlgorithm: str | None = None,
        SSECustomerKey: str | None = None,
        SSECustomerKeyMD5: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def upload_part_copy(
        self,
        *,
        Bucket: str,
        CopySource: str,
        Key: str,
        PartNumber: int,
        UploadId: str,
        CopySourceIfMatch: str | None = None,
        CopySourceIfModifiedSince: datetime.datetime | str | None = None,
        CopySourceIfNoneMatch: str | None = None,
        CopySourceIfUnmodifiedSince: datetime.datetime | str | None = None,
        CopySourceRange: str | None = None,
        SSECustomerAlgorithm: str | None = None,
        SSECustomerKey: str | None = None,
        SSECustomerKeyMD5: str | None = None,
        CopySourceSSECustomerAlgorithm: str | None = None,
        CopySourceSSECustomerKey: str | None = None,
        CopySourceSSECustomerKeyMD5: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
        ExpectedSourceBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def upload_fileobj(
        self,
        Fileobj: BinaryIO,
        Bucket: str,
        Key: str,
        ExtraArgs: dict[str, Any] | None = None,
        Callback: Callable[[int], None] | None = None,
        Config: TransferConfig | None = None,
    ) -> None:
        pass

    @abstractmethod
    def upload_file(
        self,
        Filename: str,
        Bucket: str,
        Key: str,
        ExtraArgs: dict[str, Any] | None = None,
        Callback: Callable[[int], None] | None = None,
        Config: TransferConfig | None = None,
    ) -> None:
        pass

    @abstractmethod
    def download_fileobj(
        self,
        Bucket: str,
        Key: str,
        Fileobj: BinaryIO,
        ExtraArgs: dict[str, Any] | None = None,
        Callback: Callable[[int], None] | None = None,
        Config: TransferConfig | None = None,
    ) -> None:
        pass

    @abstractmethod
    def download_file(
        self,
        Bucket: str,
        Key: str,
        Filename: str,
        ExtraArgs: dict[str, Any] | None = None,
        Callback: Callable[[int], None] | None = None,
        Config: TransferConfig | None = None,
    ) -> None:
        pass

    @abstractmethod
    def list_directory_buckets(
        self,
        *,
        ContinuationToken: str | None = None,
        MaxDirectoryBuckets: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_object_versions(
        self,
        *,
        Bucket: str,
        Delimiter: str | None = None,
        EncodingType: str | None = None,
        KeyMarker: str | None = None,
        MaxKeys: int | None = None,
        Prefix: str | None = None,
        VersionIdMarker: str | None = None,
        ExpectedBucketOwner: str | None = None,
        RequestPayer: str | None = None,
        OptionalObjectAttributes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: dict[str, Any] | None = None,
        ExpiresIn: int = 3600,
        HttpMethod: str | None = None,
    ) -> str:
        pass

    @abstractmethod
    def generate_presigned_post(
        self,
        Bucket: str,
        Key: str,
        Fields: dict[str, Any] | None = None,
        Conditions: list[Any] | None = None,
        ExpiresIn: int = 3600,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_object(
        self,
        *,
        Bucket: str,
        CopySource: str | dict[str, Any],
        Key: str,
        ACL: str | None = None,
        CacheControl: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ContentDisposition: str | None = None,
        ContentEncoding: str | None = None,
        ContentLanguage: str | None = None,
        ContentType: str | None = None,
        CopySourceIfMatch: str | None = None,
        CopySourceIfModifiedSince: datetime.datetime | str | None = None,
        CopySourceIfNoneMatch: str | None = None,
        CopySourceIfUnmodifiedSince: datetime.datetime | str | None = None,
        Expires: datetime.datetime | str | None = None,
        GrantFullControl: str | None = None,
        GrantRead: str | None = None,
        GrantReadACP: str | None = None,
        GrantWriteACP: str | None = None,
        IfMatch: str | None = None,
        IfNoneMatch: str | None = None,
        Metadata: dict[str, str] | None = None,
        MetadataDirective: str | None = None,
        TaggingDirective: str | None = None,
        AnnotationDirective: str | None = None,
        ServerSideEncryption: str | None = None,
        StorageClass: str | None = None,
        WebsiteRedirectLocation: str | None = None,
        SSECustomerAlgorithm: str | None = None,
        SSECustomerKey: str | None = None,
        SSECustomerKeyMD5: str | None = None,
        SSEKMSKeyId: str | None = None,
        SSEKMSEncryptionContext: str | None = None,
        BucketKeyEnabled: bool | None = None,
        CopySourceSSECustomerAlgorithm: str | None = None,
        CopySourceSSECustomerKey: str | None = None,
        CopySourceSSECustomerKeyMD5: str | None = None,
        RequestPayer: str | None = None,
        Tagging: str | None = None,
        ObjectLockMode: str | None = None,
        ObjectLockRetainUntilDate: datetime.datetime | str | None = None,
        ObjectLockLegalHoldStatus: str | None = None,
        ObjectLockEventHold: str | None = None,
        ObjectLockEventHoldDurationDays: int | None = None,
        ObjectLockEventHoldDurationYears: int | None = None,
        ExpectedBucketOwner: str | None = None,
        ExpectedSourceBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy(
        self,
        CopySource: dict[str, Any],
        Bucket: str,
        Key: str,
        ExtraArgs: dict[str, Any] | None = None,
        Callback: Callable[[int], None] | None = None,
        SourceClient: Any = None,
        Config: TransferConfig | None = None,
    ) -> None:
        pass

    @abstractmethod
    def get_bucket_versioning(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_versioning(
        self,
        *,
        Bucket: str,
        VersioningConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        MFA: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_tagging(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_object_tagging(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str | None = None,
        ExpectedBucketOwner: str | None = None,
        RequestPayer: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_tagging(
        self,
        *,
        Bucket: str,
        Tagging: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_object_tagging(
        self,
        *,
        Bucket: str,
        Key: str,
        Tagging: dict[str, Any],
        VersionId: str | None = None,
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
        RequestPayer: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_tagging(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_object_tagging(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_location(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_policy(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_policy(
        self,
        *,
        Bucket: str,
        Policy: str,
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ConfirmRemoveSelfBucketAccess: bool | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_policy(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_policy_status(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_encryption(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_encryption(
        self,
        *,
        Bucket: str,
        ServerSideEncryptionConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_encryption(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_public_access_block(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_public_access_block(
        self,
        *,
        Bucket: str,
        PublicAccessBlockConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_public_access_block(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_lifecycle_configuration(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_lifecycle_configuration(
        self,
        *,
        Bucket: str,
        ChecksumAlgorithm: str | None = None,
        LifecycleConfiguration: dict[str, Any] | None = None,
        ExpectedBucketOwner: str | None = None,
        TransitionDefaultMinimumObjectSize: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_lifecycle(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_cors(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_cors(
        self,
        *,
        Bucket: str,
        CORSConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_cors(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_ownership_controls(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_ownership_controls(
        self,
        *,
        Bucket: str,
        OwnershipControls: dict[str, Any],
        ContentMD5: str | None = None,
        ExpectedBucketOwner: str | None = None,
        ChecksumAlgorithm: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_ownership_controls(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_acl(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_acl(
        self,
        *,
        Bucket: str,
        ACL: str | None = None,
        AccessControlPolicy: dict[str, Any] | None = None,
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        GrantFullControl: str | None = None,
        GrantRead: str | None = None,
        GrantReadACP: str | None = None,
        GrantWrite: str | None = None,
        GrantWriteACP: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_logging(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_logging(
        self,
        *,
        Bucket: str,
        BucketLoggingStatus: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_notification_configuration(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_notification_configuration(
        self,
        *,
        Bucket: str,
        NotificationConfiguration: dict[str, Any],
        ExpectedBucketOwner: str | None = None,
        SkipDestinationValidation: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_accelerate_configuration(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
        RequestPayer: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_accelerate_configuration(
        self,
        *,
        Bucket: str,
        AccelerateConfiguration: dict[str, Any],
        ExpectedBucketOwner: str | None = None,
        ChecksumAlgorithm: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_website(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_website(
        self,
        *,
        Bucket: str,
        WebsiteConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_website(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_request_payment(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_request_payment(
        self,
        *,
        Bucket: str,
        RequestPaymentConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_object_acl(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_object_acl(
        self,
        *,
        Bucket: str,
        Key: str,
        ACL: str | None = None,
        AccessControlPolicy: dict[str, Any] | None = None,
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        GrantFullControl: str | None = None,
        GrantRead: str | None = None,
        GrantReadACP: str | None = None,
        GrantWrite: str | None = None,
        GrantWriteACP: str | None = None,
        RequestPayer: str | None = None,
        VersionId: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_object_attributes(
        self,
        *,
        Bucket: str,
        Key: str,
        ObjectAttributes: list[str],
        VersionId: str | None = None,
        MaxParts: int | None = None,
        PartNumberMarker: int | None = None,
        SSECustomerAlgorithm: str | None = None,
        SSECustomerKey: str | None = None,
        SSECustomerKeyMD5: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_object_legal_hold(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_object_legal_hold(
        self,
        *,
        Bucket: str,
        Key: str,
        LegalHold: dict[str, Any] | None = None,
        RequestPayer: str | None = None,
        VersionId: str | None = None,
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_object_retention(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_object_retention(
        self,
        *,
        Bucket: str,
        Key: str,
        Retention: dict[str, Any] | None = None,
        RequestPayer: str | None = None,
        VersionId: str | None = None,
        BypassGovernanceRetention: bool | None = None,
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_object_lock_configuration(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_object_lock_configuration(
        self,
        *,
        Bucket: str,
        ObjectLockConfiguration: dict[str, Any] | None = None,
        RequestPayer: str | None = None,
        Token: str | None = None,
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_object(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str | None = None,
        RestoreRequest: dict[str, Any] | None = None,
        RequestPayer: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_bucket_metadata_configuration(
        self,
        *,
        Bucket: str,
        MetadataConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_bucket_metadata_table_configuration(
        self,
        *,
        Bucket: str,
        MetadataTableConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_session(
        self,
        *,
        Bucket: str,
        SessionMode: str | None = None,
        ServerSideEncryption: str | None = None,
        SSEKMSKeyId: str | None = None,
        SSEKMSEncryptionContext: str | None = None,
        BucketKeyEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_analytics_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_intelligent_tiering_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_inventory_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_metadata_configuration(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_metadata_table_configuration(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_metrics_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_replication(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_object_annotation(
        self,
        *,
        Bucket: str,
        Key: str,
        AnnotationName: str,
        VersionId: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
        ObjectIfMatch: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_abac(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_analytics_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_intelligent_tiering_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_inventory_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_lifecycle(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_metadata_configuration(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_metadata_table_configuration(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_metrics_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_notification(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_replication(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_object_annotation(
        self,
        *,
        Bucket: str,
        Key: str,
        AnnotationName: str,
        VersionId: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
        ChecksumMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_object_torrent(
        self,
        *,
        Bucket: str,
        Key: str,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bucket_analytics_configurations(
        self,
        *,
        Bucket: str,
        ContinuationToken: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bucket_intelligent_tiering_configurations(
        self,
        *,
        Bucket: str,
        ContinuationToken: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bucket_inventory_configurations(
        self,
        *,
        Bucket: str,
        ContinuationToken: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bucket_metrics_configurations(
        self,
        *,
        Bucket: str,
        ContinuationToken: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_object_annotations(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str | None = None,
        MaxAnnotationResults: int | None = None,
        AnnotationPrefix: str | None = None,
        ContinuationToken: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_objects(
        self,
        *,
        Bucket: str,
        Delimiter: str | None = None,
        EncodingType: str | None = None,
        Marker: str | None = None,
        MaxKeys: int | None = None,
        Prefix: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
        OptionalObjectAttributes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_abac(
        self,
        *,
        Bucket: str,
        AbacStatus: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_analytics_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        AnalyticsConfiguration: dict[str, Any],
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_intelligent_tiering_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        IntelligentTieringConfiguration: dict[str, Any],
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_inventory_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        InventoryConfiguration: dict[str, Any],
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_lifecycle(
        self,
        *,
        Bucket: str,
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        LifecycleConfiguration: dict[str, Any] | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_metrics_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        MetricsConfiguration: dict[str, Any],
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_notification(
        self,
        *,
        Bucket: str,
        NotificationConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_replication(
        self,
        *,
        Bucket: str,
        ReplicationConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        Token: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_object_annotation(
        self,
        *,
        Bucket: str,
        Key: str,
        AnnotationName: str,
        AnnotationPayload: bytes | BinaryIO | str,
        VersionId: str | None = None,
        ObjectIfMatch: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ChecksumCRC32: str | None = None,
        ChecksumCRC32C: str | None = None,
        ChecksumCRC64NVME: str | None = None,
        ChecksumSHA1: str | None = None,
        ChecksumSHA256: str | None = None,
        ChecksumSHA512: str | None = None,
        ChecksumMD5: str | None = None,
        ChecksumXXHASH64: str | None = None,
        ChecksumXXHASH3: str | None = None,
        ChecksumXXHASH128: str | None = None,
        ContentMD5: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def rename_object(
        self,
        *,
        Bucket: str,
        Key: str,
        RenameSource: str,
        DestinationIfMatch: str | None = None,
        DestinationIfNoneMatch: str | None = None,
        DestinationIfModifiedSince: datetime.datetime | str | None = None,
        DestinationIfUnmodifiedSince: datetime.datetime | str | None = None,
        SourceIfMatch: str | None = None,
        SourceIfNoneMatch: str | None = None,
        SourceIfModifiedSince: datetime.datetime | str | None = None,
        SourceIfUnmodifiedSince: datetime.datetime | str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def select_object_content(
        self,
        *,
        Bucket: str,
        Key: str,
        Expression: str,
        ExpressionType: str,
        InputSerialization: dict[str, Any],
        OutputSerialization: dict[str, Any],
        SSECustomerAlgorithm: str | None = None,
        SSECustomerKey: str | None = None,
        SSECustomerKeyMD5: str | None = None,
        RequestProgress: dict[str, Any] | None = None,
        ScanRange: dict[str, Any] | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_bucket_metadata_annotation_table_configuration(
        self,
        *,
        Bucket: str,
        AnnotationTableConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_bucket_metadata_inventory_table_configuration(
        self,
        *,
        Bucket: str,
        InventoryTableConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_bucket_metadata_journal_table_configuration(
        self,
        *,
        Bucket: str,
        JournalTableConfiguration: dict[str, Any],
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_object_encryption(
        self,
        *,
        Bucket: str,
        Key: str,
        ObjectEncryption: dict[str, Any],
        VersionId: str | None = None,
        RequestPayer: str | None = None,
        ExpectedBucketOwner: str | None = None,
        ContentMD5: str | None = None,
        ChecksumAlgorithm: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def write_get_object_response(
        self,
        *,
        RequestRoute: str,
        RequestToken: str,
        Body: bytes | BinaryIO | str | None = None,
        StatusCode: int | None = None,
        ErrorCode: str | None = None,
        ErrorMessage: str | None = None,
        AcceptRanges: str | None = None,
        CacheControl: str | None = None,
        ContentDisposition: str | None = None,
        ContentEncoding: str | None = None,
        ContentLanguage: str | None = None,
        ContentLength: int | None = None,
        ContentRange: str | None = None,
        ContentType: str | None = None,
        ChecksumCRC32: str | None = None,
        ChecksumCRC32C: str | None = None,
        ChecksumCRC64NVME: str | None = None,
        ChecksumSHA1: str | None = None,
        ChecksumSHA256: str | None = None,
        ChecksumSHA512: str | None = None,
        ChecksumMD5: str | None = None,
        ChecksumXXHASH64: str | None = None,
        ChecksumXXHASH3: str | None = None,
        ChecksumXXHASH128: str | None = None,
        DeleteMarker: bool | None = None,
        ETag: str | None = None,
        Expires: datetime.datetime | str | None = None,
        Expiration: str | None = None,
        LastModified: datetime.datetime | str | None = None,
        MissingMeta: int | None = None,
        Metadata: dict[str, str] | None = None,
        ObjectLockMode: str | None = None,
        ObjectLockLegalHoldStatus: str | None = None,
        ObjectLockRetainUntilDate: datetime.datetime | str | None = None,
        PartsCount: int | None = None,
        ReplicationStatus: str | None = None,
        RequestCharged: str | None = None,
        Restore: str | None = None,
        ServerSideEncryption: str | None = None,
        SSECustomerAlgorithm: str | None = None,
        SSEKMSKeyId: str | None = None,
        SSECustomerKeyMD5: str | None = None,
        StorageClass: str | None = None,
        TagCount: int | None = None,
        VersionId: str | None = None,
        BucketKeyEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
