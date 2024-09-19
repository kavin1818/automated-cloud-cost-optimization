"""
Flask Web Application for Cloud Cost Optimization Tool
This module serves a web interface that displays resource usage, trends, and recommendations.
"""
from flask import Flask, render_template
from cost_analysis.optimizer import CostOptimizer
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    """
    Renders the dashboard page with current resource usage and recommendations.
    
    Returns:
        HTML: Rendered HTML page with resource usage and cost-saving recommendations.
    """
    # Dummy Data
    data = pd.DataFrame({
        'instance_id': ['i-123', 'i-456'],
        'cpu_usage': [10, 80],
        'memory_usage': [15, 90],
        'cost': [5.00, 10.00]
    })
    
    optimizer = CostOptimizer(data)
    recommendations = optimizer.rightsizing_recommendation()
    projected_cost = optimizer.cost_projection()

    return render_template('dashboard.html', recommendations=recommendations, projected_cost=projected_cost)

if __name__ == "__main__":
    app.run(debug=True)
