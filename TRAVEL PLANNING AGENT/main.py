from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from agents.agent_store import planner_agent, local_agent, language_agent, travel_summary_agent
from autogen_agentchat.ui import Console
import asyncio

termination = TextMentionTermination("TERMINATE")
group_chat = RoundRobinGroupChat(
    participants=[planner_agent, local_agent, language_agent, travel_summary_agent],
    termination_condition=termination,
    max_turns=4
)

async def main(): 
    stream = group_chat.run_stream(
        task="Plan a 3 day trip to Delhi",
    )    
    await Console(stream)
    
if __name__=="__main__":
    asyncio.run(main())
    
