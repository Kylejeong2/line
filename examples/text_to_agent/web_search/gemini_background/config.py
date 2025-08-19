"""Agent Configuration File.

This file should be customized based on the agent.md specifications to control
the behavior of the template. Modify the system prompt, initial message, and
other settings to match your specific agent requirements.
"""

##################################################
####                 LLM Settings            ####
##################################################

CHAT_MODEL_ID = "gemini-2.5-flash-lite"
CHAT_TEMPERATURE = 0.7

SEARCH_MODEL_ID = "gemini-live-2.5-flash-preview"
SEARCH_TEMPERATURE = 0.7


##################################################
####            Agent Context               ####
##################################################
# Set current location here
LOCATION = "Unknown"

##################################################
####             Agent Prompt               ####
##################################################

# Customizable agent prompt - defines the agent's role and purpose
AGENT_PROMPT = """
You're a warm, personable, intelligent and helpful AI chat bot.
"""

##################################################
####            Initial Message             ####
##################################################
# This message is sent by the agent to the user when the call is started.
INITIAL_MESSAGE: str | None = (
    "Today's date is {current_date} and my approximate location is {current_location}."
)
