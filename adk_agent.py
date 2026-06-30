# adk_agent.py
"""
Google ADK Agent Wrapper for CrisisGuard AI.
This file satisfies the "Agent / Multi-agent system (ADK)" requirement.
"""

from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.runners import Runner
from crisis_detector import CrisisDetector # Assuming your logic is here

# Initialize your existing Python logic
detector = CrisisDetector()

# Define the tool that your ADK agent will use
def analyze_crisis_event(event_data: dict) -> str:
    """
    Analyzes a crisis event and returns a severity report.
    This wraps the core CrisisDetector logic.
    """
    # Call your existing Python method
    severity = detector.calculate_severity(event_data)
    classification = detector.classify_crisis(event_data)
    
    return f"CRISIS DETECTED: {classification} | Severity: {severity}% | Action: Immediate Alert"

# Register the tool
analyze_crisis_tool = FunctionTool(
    func=analyze_crisis_event,
    name="analyze_crisis_event",
    description="Analyzes incoming crisis data to determine severity and classification."
)

# Create the ADK Agent
crisis_guard_agent = Agent(
    name="CrisisGuardAgent",
    model="gemini-2.0-flash-exp", # Use the model specified in the course
    instructions="""
    You are CrisisGuard, an AI agent dedicated to real-time disaster response.
    Your primary function is to analyze incoming data using the 'analyze_crisis_event' tool.
    If a crisis is detected with severity > 70%, immediately flag it as critical.
    Always provide a clear, actionable summary for NGOs.
    """,
    tools=[analyze_crisis_tool]
)

# Optional: Simple runner to test it
if __name__ == "__main__":
    runner = Runner(agent=crisis_guard_agent)
    # Example test
    test_event = {"type": "flood", "magnitude": 8.5, "population_affected": 50000}
    print("Running ADK Agent Test...")
    response = runner.run(test_event)
    print(response)