from autogen_core.tools import FunctionTool

def save_report(content: str, filename: str = "travel_itinerary.md") -> str:
    """
    Save content to a markdown file.
    
    Args:
        content: The content to save (markdown formatted text)
        filename: The name of the file to save (default: "travel_itinerary.md")
    
    Returns:
        A confirmation message indicating the file was saved
    """    
    import os
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    agent_dir = os.path.dirname(current_dir)
    full_path = os.path.join(agent_dir, filename)
    
    # Write the content to the file
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return f"Report successfully saved to {full_path}"

save_report_tool = FunctionTool(
    save_report, description="Save a report or content to a markdown file. Use this to save the final travel planning report."
)
