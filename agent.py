import autogen
from autogen import ConversableAgent
from config import llm_config, DEFAULT_DATASET_PATH
from system_messages import *
from utlis import *

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"use_docker": False},
    llm_config=llm_config,
    system_message=USER_PROXY_SYSTEM_MESSAGE
)

Data_source_Agent = autogen.AssistantAgent(
    "Data_source_Agent",
    llm_config=llm_config,
    system_message=DATA_SOURCE_SYSTEM_MESSAGE,
)

user_proxy.register_for_execution()(download_dataset_via_git)
Data_source_Agent.register_for_llm(description="Download Hugging Face datasets using git clone and Git LFS.")(download_dataset_via_git)

locater = autogen.AssistantAgent(
    "locater",
    llm_config=llm_config,
    system_message=LOCATER_SYSTEM_MESSAGE,
)

user_proxy.register_for_execution()(get_dataset_file_paths)
locater.register_for_llm(description="Find all relevant files in a dataset directory.")(get_dataset_file_paths)

EDA_agent = autogen.AssistantAgent(
    name="EDA_agent",
    llm_config=llm_config,
    system_message=EDA_SYSTEM_MESSAGE
)

assistant_EDA = ConversableAgent(
    "assistant_EDA",
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    system_message=ASSISTANT_EDA_SYSTEM_MESSAGE
)

EDA_agent.register_nested_chats(
    [
        {
            "recipient": assistant_EDA,
            "summary_method": "last_msg",
            "message": reflection_message,
            "max_turns": 1,
        }
    ],
    trigger=lambda sender: sender is user_proxy and triggered(sender),
)

visualization_AGENT = autogen.AssistantAgent(
    name="visualization_AGENT",
    llm_config=llm_config,
    system_message=VISUALIZATION_SYSTEM_MESSAGE
)

visualization_interpreter = ConversableAgent(
    "visualization_interpreter",
    llm_config=llm_config,
    human_input_mode="NEVER",
    system_message=VISUALIZATION_INTERPRETER_SYSTEM_MESSAGE
)

visualization_AGENT.register_nested_chats(
    [
        {
            "recipient": visualization_interpreter,
            "summary_method": "last_msg",
            "message": visualization_reflection_message,
            "max_turns": 1,
        }
    ],
    trigger=lambda sender: sender is user_proxy and visualization_trigger(sender),
)

Report_generation_agent = autogen.AssistantAgent(
    name="Report_generation_agent",
    llm_config=llm_config,
    system_message=REPORT_GENERATION_SYSTEM_MESSAGE
)

agents = {
    'user_proxy': user_proxy,
    'data_source': Data_source_Agent,
    'locater': locater,
    'eda_agent': EDA_agent,
    'assistant_eda': assistant_EDA,
    'visualization_agent': visualization_AGENT,
    'visualization_interpreter': visualization_interpreter,
    'report_generation_agent': Report_generation_agent
}