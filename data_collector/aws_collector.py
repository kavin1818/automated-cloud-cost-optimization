"""
AWS Data Collector
This module collects AWS cloud resource usage using Boto3 and stores the data for analysis.
"""
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

class AWSDataCollector:
    """
    Collects usage metrics from AWS using Boto3.
    
    Attributes:
        ec2_client (boto3.client): AWS EC2 client for interacting with EC2 resources.
        cloudwatch_client (boto3.client): AWS CloudWatch client for fetching metrics.
    """
    
    def __init__(self):
        # self.ec2_client = boto3.client('ec2')
        # self.cloudwatch_client = boto3.client('cloudwatch')
        self.aws_access_key = os.getenv('AWS_ACCESS_KEY')
        self.aws_secret_key = os.getenv('AWS_SECRET_KEY')
        self.session = boto3.Session(
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_key,
        )
        self.ec2 = self.session.client('ec2')

    def get_ec2_instances(self):
        """
        Retrieves EC2 instance details including usage metrics.
        
        Returns:
            list: List of EC2 instance details with CPU and memory utilization.
        """
        try:
            instances = self.ec2_client.describe_instances()
            metrics = self.cloudwatch_client.get_metric_data(
                MetricDataQueries=[
                    # Example metric query for CPU utilization
                ],
                StartTime=datetime.utcnow() - timedelta(days=1),
                EndTime=datetime.utcnow(),
                Period=3600
            )
            return instances['Reservations'], metrics
        except ClientError as error:
            print(f"An error occurred: {error}")
            return []

    # Add more AWS services methods here

if __name__ == "__main__":
    aws_collector = AWSDataCollector()
    ec2_data = aws_collector.get_ec2_instances()
    print(ec2_data)
