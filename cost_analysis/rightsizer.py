"""
Rightsizer
This module analyzes resource usage data and provides rightsizing recommendations to optimize costs.
"""

import pandas as pd


class Rightsizer:
    """
    Provides rightsizing recommendations based on resource utilization.
    
    Attributes:
        usage_data (pd.DataFrame): DataFrame containing resource usage information.
    """
    
    def __init__(self, usage_data: pd.DataFrame):
        self.usage_data = usage_data

    def recommend_rightsizing(self):
        """
        Recommends rightsizing actions based on CPU and memory usage thresholds.
        
        Returns:
            pd.DataFrame: DataFrame containing rightsizing recommendations.
        """
        underutilized = self.usage_data[
            (self.usage_data['cpu_usage'] < 20) | (self.usage_data['memory_usage'] < 30)
        ]
        
        if underutilized.empty:
            return pd.DataFrame({'message': ['No rightsizing recommendations at this time']})
        return underutilized[['instance_id', 'cpu_usage', 'memory_usage']]


if __name__ == "__main__":
    # Example usage
    data = pd.DataFrame({
        'instance_id': ['i-123', 'i-456'],
        'cpu_usage': [10, 80],
        'memory_usage': [25, 90]
    })
    
    rightsizer = Rightsizer(data)
    print(rightsizer.recommend_rightsizing())
