import os
import subprocess
from typing import List, Dict
from typing_extensions import Annotated
from fpdf import FPDF
import os

def download_dataset_via_git(
    repo_url: Annotated[str, "The Hugging Face dataset repository URL."],
    local_path: Annotated[str, "Directory to save the cloned dataset."] = "C:\\Users\\Aryan Gurav\\Desktop\\AGENTIC_CLEAN\\dataset"
) -> str:
    try:
        local_path = os.path.abspath(local_path)
        os.makedirs(local_path, exist_ok=True)
        subprocess.run(["git", "lfs", "install"], check=True)
        subprocess.run(["git", "clone", repo_url, local_path], check=True)
        return f"Dataset successfully cloned to {local_path}"
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Error during Git or Git LFS operations: {e}")
    except Exception as e:
        raise ValueError(f"Unexpected error: {e}")

def get_dataset_file_paths(
    dataset_path: Annotated[str, "Dataset Path"],
    file_extensions: str = None
) -> Dict[str, List[str]]:
    try:
        if not os.path.exists(dataset_path):
            raise ValueError(f"Dataset path does not exist: {dataset_path}")
        
        file_paths = {}
        for root, _, files in os.walk(dataset_path):
            if '.git' in root:
                continue
            
            for filename in files:
                full_path = os.path.join(root, filename)
                file_ext = os.path.splitext(filename)[1].lower()
                
                if file_extensions is None or file_ext in file_extensions:
                    if file_ext not in file_paths:
                        file_paths[file_ext] = []
                    file_paths[file_ext].append(full_path)
        
        return file_paths
    except Exception as e:
        raise ValueError(f"Error finding dataset files: {e}")

def get_visualization_images(visualizations_dir: str) -> List[str]:
    try:
        if not os.path.exists(visualizations_dir):
            print(f"Visualization directory not found: {visualizations_dir}")
            return []
        
        png_files = [
            os.path.join(visualizations_dir, file) 
            for file in os.listdir(visualizations_dir) 
            if file.lower().endswith('.png')
        ]
        
        return png_files
    except Exception as e:
        print(f"Error retrieving visualization images: {e}")
        return []

def triggered(sender):
    try:
        print("Checking trigger condition...")
        
        if not hasattr(sender, '_nested_chat_triggered'):
            sender._nested_chat_triggered = False
        
        if hasattr(sender, 'chat_messages') and sender.chat_messages:
            last_conversation = list(sender.chat_messages.keys())[-1]
            messages = sender.chat_messages[last_conversation]
            
            message_contents = [message.get('content', '') for message in messages]
            all_messages = " ".join(message_contents)
            
            success_marker = "code89298"
            failure_indicators = ["Error", "Failed", "Exception"]
            
            is_triggered = (
                success_marker.lower() in all_messages.lower() and 
                not any(f.lower() in all_messages.lower() for f in failure_indicators) and
                not sender._nested_chat_triggered
            )
            
            if is_triggered:
                sender._nested_chat_triggered = True
            
            print(f"Trigger condition result: {is_triggered}")
            return is_triggered
        
        print("No chat messages found")
        return False
    except Exception as e:
        print(f"Error in triggered function: {e}")
        return False

def visualization_trigger(sender):
    try:
        print("Checking trigger condition...")
        if not hasattr(sender, '_nested_chat_triggered'):
            sender._nested_chat_triggered = False
        
        if hasattr(sender, 'chat_messages') and sender.chat_messages:
            last_conversation = list(sender.chat_messages.keys())[-1]
            messages = sender.chat_messages[last_conversation]
            
            message_contents = [message.get('content', '') for message in messages]
            all_messages = " ".join(message_contents)
            
            success_marker = "Code89284"
            failure_indicators = ["Error", "Failed", "Exception"]
            
            is_triggered = (
                success_marker.lower() in all_messages.lower() and 
                not any(f.lower() in all_messages.lower() for f in failure_indicators) and
                not sender._nested_chat_triggered
            )
            
            if is_triggered:
                sender._nested_chat_triggered = True
            
            print(f"Trigger condition result: {is_triggered}")
            return is_triggered
        
        print("No chat messages found")
        return False
    except Exception as e:
        print(f"Error in triggered function: {e}")
        return False

def reflection_message(recipient, messages, sender, config):
    return f"Write and execute the EDA for the dataset \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}"

def visualization_reflection_message(recipient, messages, sender, config):
    visualizations_dir = os.path.join("dataset", 'visualizations')
    visualization_images = get_visualization_images(visualizations_dir)
    return f"""Analyze and provide comprehensive insights for the following visualizations:
        Key Analysis Requirements:
            - Examine each visualization carefully
            - Identify patterns, trends, and significant insights
            - Provide statistical and contextual interpretations
            - Highlight potential business or research implications
        Visualization Images:
            {chr(10).join(visualization_images)}
        Please systematically analyze each visualization, referencing the image file paths.""" 

