import boto3

s3 = boto3.resource('s3')

# Check if bucket is publicly accessible
bucket = s3.Bucket('your-bucket-name')
acl = bucket.Acl()
for grant in acl.grants:
    if grant['Grantee']['Type'] == 'Group' and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
        print('Warning: S3 bucket is publicly accessible.')

# Check if bucket has server-side encryption enabled
encryption = bucket.Encryption()
if not encryption:
    print('Warning: Server-side encryption is not enabled for S3 bucket.')

# Check if bucket has versioning enabled
versioning = bucket.Versioning()
if not versioning:
    print('Warning: Versioning is not enabled for S3 bucket.')

# Check if bucket has a bucket policy set
policy = bucket.Policy()
if not policy:
    print('Warning: S3 bucket does not have a bucket policy set.')
