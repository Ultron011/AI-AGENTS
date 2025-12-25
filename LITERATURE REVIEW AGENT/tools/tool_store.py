from autogen_core.tools import FunctionTool

def tavily_search(query: str, num_results: int = 2, max_chars: int = 500) -> list:
    from tavily import TavilyClient

    client = TavilyClient()
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=num_results,
        include_answer=False,
        include_raw_content=False
    )

    enriched_results = []
    for item in response.get("results", []):
        content = item.get("content", "")[:max_chars]

        enriched_results.append({
            "title": item.get("title"),
            "link": item.get("url"),
            "snippet": item.get("content", "")[:200],
            "body": content
        })

    return enriched_results

def arxiv_search(query: str, max_results: int = 2) -> list:
    """
    Search Arxiv for papers and return the results including abstracts.
    """

    import arxiv
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    results = []
    for paper in client.results(search):
        results.append({
            "title": paper.title,
            "authors": [author.name for author in paper.authors],
            "published": paper.published.strftime("%Y-%m-%d"),
            "abstract": paper.summary,
            "pdf_url": paper.pdf_url
        })

    return results

def save_report(content: str, filename: str = "literature_review.md") -> str:
    """
    Save content to a markdown file.
    
    Args:
        content: The content to save (markdown formatted text)
        filename: The name of the file to save (default: "literature_review.md")
    
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

google_search_tool = FunctionTool(
    tavily_search, description="Search Google for information, returns results with a snippet and body content"
)
arxiv_search_tool = FunctionTool(
    arxiv_search, description="Search Arxiv for papers related to a given topic, including abstracts"
)
save_report_tool = FunctionTool(
    save_report, description="Save a report or content to a markdown file. Use this to save the final literature review report."
)
