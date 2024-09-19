"""
Scheduler
This module implements a scheduling mechanism to periodically collect cloud usage data.
"""

import schedule
import time
import os
from dotenv import load_dotenv
from data_collector.aws_collector import AWSDataCollector
from data_collector.azure_collector import AzureDataCollector
from data_collector.gcp_collector import GCPDataCollector

# Load environment variables from .env file
load_dotenv()

class DataCollectionScheduler:
    """
    Schedules periodic data collection tasks for cloud providers.
    
    Attributes:
        aws_collector (AWSDataCollector): Instance of the AWS data collector.
        azure_collector (AzureDataCollector): Instance of the Azure data collector.
        gcp_collector (GCPDataCollector): Instance of the GCP data collector.
    """
    
    def __init__(self, aws_subscription, azure_subscription, gcp_project, gcp_credentials):
        self.aws_collector = AWSDataCollector()
        self.azure_collector = AzureDataCollector(azure_subscription)
        self.gcp_collector = GCPDataCollector(gcp_project, gcp_credentials)
    
    def collect_aws_data(self):
        """
        Collects and processes AWS resource usage data.
        """
        aws_data = self.aws_collector.get_ec2_instances()
        print("AWS Data Collected:", aws_data)

    def collect_azure_data(self):
        """
        Collects and processes Azure resource usage data.
        """
        azure_data = self.azure_collector.get_vm_instances()
        print("Azure Data Collected:", azure_data)

    def collect_gcp_data(self):
        """
        Collects and processes GCP resource usage data.
        """
        gcp_data = self.gcp_collector.get_vm_instances('us-central1-a')
        print("GCP Data Collected:", gcp_data)

    def schedule_tasks(self):
        """
        Schedules data collection tasks at regular intervals.
        """
        schedule.every().day.at("00:00").do(self.collect_aws_data)
        schedule.every().day.at("01:00").do(self.collect_azure_data)
        schedule.every().day.at("02:00").do(self.collect_gcp_data)

        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    # Setup the scheduler
    aws_subscription = os.getenv('AWS_SUBSCRIPTION_ID')
    azure_subscription = os.getenv('AZURE_SUBSCRIPTION_ID')
    gcp_project = os.getenv('GCP_PROJECT_ID')
    gcp_credentials = os.getenv('GCP_CREDENTIALS')
    
    scheduler = DataCollectionScheduler(aws_subscription, azure_subscription, gcp_project, gcp_credentials)
    scheduler.schedule_tasks()
