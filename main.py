from agent import user_proxy, Data_source_Agent, locater, EDA_agent, visualization_AGENT, Report_generation_agent

def initiate_sequential_workflow(dataset_url):
    print("Step 1: Downloading dataset...")
    dataset_path = user_proxy.initiate_chats(
        [{
            "recipient": Data_source_Agent,
            "message": "Download the dataset from " + dataset_url,
            "summary_method": "reflection_with_llm"
        }]
    )

    print("Step 2: Locating files...")
    file_paths = user_proxy.initiate_chats(
        [{
            "recipient": locater,
            "message": f"Find all files in the dataset directory at {str(dataset_path)}",
            "summary_method": "reflection_with_llm"
        }]
    )

    print("Step 3: Performing EDA...")
    user_proxy.initiate_chats(
        [{
            "recipient": EDA_agent,
            "message": "Perform Exploratory Data Analysis on the dataset",
            "carryover": f"File paths:{str(file_paths)}",
            "summary_method": "reflection_with_llm"
        }]
    )

    print("Step 4: Creating visualizations...")
    user_proxy.initiate_chats(
        [{
            "recipient": visualization_AGENT,
            "message": "Generate visualizations based on EDA insights",
            "carryover": f"File paths:{str(file_paths)}",
            "summary_method": "reflection_with_llm"
        }]
    )

    print("Step 5: Generating final report...")
    user_proxy.initiate_chats(
        [{
            "recipient": Report_generation_agent,
            "message": "Create a comprehensive report",
            "carryover": f"Dataset path:{str(dataset_path)} File paths:{str(file_paths)}",
            "summary_method": "reflection_with_llm"
        }]
    )

    print("Workflow completed successfully!")

if __name__ == "__main__":

    dataset_url = "https://huggingface.co/datasets/positivethoughts/rewrite_10k"
    initiate_sequential_workflow(dataset_url)