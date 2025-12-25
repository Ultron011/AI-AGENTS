from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from agents.agent_store import google_search_agent, arxiv_search_agent, report_agent
from autogen_agentchat.ui import Console
import asyncio

termination = TextMentionTermination("TERMINATE")
team = RoundRobinGroupChat(
    [google_search_agent, arxiv_search_agent, report_agent],
    termination_condition=termination
)

async def main(): 
    stream = team.run_stream(
        task="Write a literature review on no code tools for building multi agent ai systems",
    )    
    await Console(stream)
    
if __name__=="__main__":
    asyncio.run(main())