# mcp_server.py
"""
MCP Server for CrisisGuard AI.
This file satisfies the "MCP Server" requirement.
"""

from mcp.server.fastmcp import FastMCP
from crisis_detector import CrisisDetector

# Initialize your core logic
detector = CrisisDetector()

# Create the MCP server
mcp = FastMCP("CrisisGuard MCP Server")

@mcp.tool()
def get_crisis_severity(event_type: str, magnitude: float, affected_population: int) -> dict:
    """
    Calculates the severity of a crisis event based on type, magnitude, and population.
    Returns a JSON object with the severity score and recommended action.
    """
    event_data = {
        "type": event_type,
        "magnitude": magnitude,
        "population_affected": affected_population
    }
    
    severity = detector.calculate_severity(event_data)
    classification = detector.classify_crisis(event_data)
    
    action = "Monitor"
    if severity > 80:
        action = "EMERGENCY DEPLOYMENT REQUIRED"
    elif severity > 50:
        action = "Immediate Assessment Needed"
    
    return {
        "severity_score": severity,
        "classification": classification,
        "recommended_action": action,
        "input_data": event_data
    }

if __name__ == "__main__":
    # Run the server
    mcp.run(transport="stdio")
    # Note: For the video, you can show the server running or calling the tool via CLI