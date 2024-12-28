from crewai import Task
from tools import tool 
from agent import * 

# Research task 
research_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points,"
        "it's market oppurtunities, and potential risks."
    ),
    expected_output = "A comprehensive 3 paragraphs long report on the latest AI trends.",
    tools=[tool],
    agent = news_researcher,
)

# Writing task with language model config
writer_task = Task(
    description=(
        "Compose an insightful article on {topic}."
        "Focus on latest trends and how it's impacting teh industry."
        "This article should be easy to understand,engaging and positive."
    ),
    expected_output = "A 1 paragraph article on {topic} advanchements formatted asmarkdown.",
    tools=[tool],
    agent = news_writer,
    async_execution=False,
    output_file="news-blog-post.md"
)