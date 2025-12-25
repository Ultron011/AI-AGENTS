from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from agents.agents import stock_analysis_agent, search_agent, report_agent
from autogen_agentchat.ui import Console
import asyncio

team = RoundRobinGroupChat([stock_analysis_agent, search_agent, report_agent], max_turns=3)

async def main(): 
    stream = team.run_stream(task="Write a financial report on American airlines")
    await Console(stream)
    
if __name__=="__main__":
    asyncio.run(main())