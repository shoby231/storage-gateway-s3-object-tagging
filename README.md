STORAGE GATEWAY FILE UPLOAD NOTIFICATION EVENT TO TAG OBJECTS IN S3

To achieve this, since File Gateway cannot out of the box tag objects written to S3, we can have a Lambda function write the tags to the objects after the File Gateway has finished uploading the objects. The Lambda function will be triggered by “Storage Gateway File Upload Event”. This event can be triggered by Cloud Event or Amazon EventBridge. The NotificationPolicy parameter will be configured to the interval you want the file gateway to check if files have been fully uploaded to the S3 bucket.

After setting the NoficationPolicy interval as shown above has been set via the file gateway console. You can create an Event using the EventBridge Service. 

Create a Lambda function and in addition to the Default permission on the Lambda function IAM role, attach the policy below;

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObjectTagging",
                "s3:GetObjectTagging",
                "s3:DeleteObjectTagging"
            ],
            "Resource": [
                "arn:aws:s3:::awsexamplebucket1/*"
            ]
        }
    ]
}

Run time should be Python 3.8 and paste the sample code in the sgw-upload.py file; Specify the KEY and VALUE in the code

Go to AWS EventBridge Service on the AWS Console, Click the Create rule button, give the rule a name for example, File-Gateway-Upload-Event. Give it a Description if you want, select the Event pattern radio button, Next select the Pre-defined pattern by service. In the Service provider drop-down list choose AWS, in the Service name drop-down, search and select Storage Gateway, for Event type drop-down select Storage Gateway Object Upload Event. Scroll down to Target and select Lambda and choose the function created earlier and click create. 

To test if the Lambda function  works, mount to the file share either from a Windows or Linux client, upload a sample file and wait for the object to get upload to the S3 and wait for the interval specified in the NotificationPolicy.

