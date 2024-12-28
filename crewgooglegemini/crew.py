from agent import *
from task import *
from crewai import Crew, Process
# Forming the tech forward crew with someenhanced config 

crew = Crew(
    agents=[news_researcher,news_writer],
    tasks = [research_task,writer_task],
    process=Process.sequential
)

# starting the task execution process with enhanced feedback

result = crew.kickoff(inputs = {"topic":"AI in healthcare"})
print(result)