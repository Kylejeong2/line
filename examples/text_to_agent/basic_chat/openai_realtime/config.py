"""Agent Configuration File.

This file should be customized based on the agent specifications to control
the behavior of the template.
"""

##################################################
####            LLM Settings                 ####
##################################################

# Model Settings for OpenAI Realtime API
CHAT_MODEL_ID = "gpt-4o-realtime-preview-2025-06-03"
CHAT_TEMPERATURE = 0.7


##################################################
####             Agent Context              ####
##################################################
# Set current location here
LOCATION = "Unknown"

##################################################
####        Agent Prompt                     ####
##################################################

# Customizable agent prompt - defines the agent's role and purpose
AGENT_PROMPT = """
You're a warm, personable, intelligent and helpful AI chat bot.
"""

##################################################
#### Initial Message                            ####
##################################################
# This message is sent by the agent to the user when the call is started.
INITIAL_MESSAGE: str | None = (
    "Today's date is {current_date} and my approximate location is {current_location}."
)
