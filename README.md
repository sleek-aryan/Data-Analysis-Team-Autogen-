# Multi-Agent Data Analysis System

## Overview
This project implements an advanced data analysis pipeline using a multi-agent system built with AutoGen. The system orchestrates multiple specialized AI agents to perform end-to-end data analysis, from dataset acquisition to report generation. Each agent has a specific role and collaborates with others to produce comprehensive analytical insights.

## System Architecture

### Agents and Their Roles

1. **Data Source Agent**
   - Downloads datasets from Hugging Face repositories
   - Handles Git LFS for large file downloads
   - Ensures proper local storage of datasets

2. **Locater Agent**
   - Scans and catalogs all files in the dataset directory
   - Filters files by extension when needed
   - Provides organized file paths to other agents

3. **EDA (Exploratory Data Analysis) Agent**
   - Performs comprehensive data analysis
   - Handles data cleaning and preprocessing
   - Generates statistical summaries
   - Creates new features when relevant
   - Saves insights to `insights.txt`

4. **EDA Interpreter Assistant**
   - Interprets EDA results
   - Provides in-depth analytical insights
   - Highlights key statistical findings
   - Identifies areas for further investigation

5. **Visualization Agent**
   - Creates multiple data visualizations (minimum 10 plots)
   - Saves visualizations as PNG files
   - Organizes outputs in a dedicated visualization directory

6. **Visualization Interpreter**
   - Analyzes generated visualizations
   - Provides detailed interpretation of patterns and trends
   - Offers contextual insights
   - Creates `plot_insights.txt` with comprehensive analysis

7. **Report Generation Agent**
   - Compiles all analyses and visualizations
   - Creates professional PDF reports
   - Structures content with clear sections
   - Handles proper formatting and layout

## Setup and Dependencies

### Required Libraries
```python
import os
import autogen
from autogen import ConversableAgent
from typing import Annotated, Dict, List, Optional
import subprocess
import tempfile
```

### Configuration
The system uses GPT-4 for agent intelligence with the following configuration:
```python
config_list = [
    {
        "model": "gpt-4o-mini-2024-07-18",
        "api_key": "your-api-key-here"
    }
]

llm_config = {
    "temperature": 0,
    "config_list": config_list,
}
```

## Workflow (SEQUENTIAL CHAT)

1. **Dataset Acquisition**
   - Downloads specified dataset from Hugging Face
   - Uses Git LFS for large files
   - Stores in local directory

2. **File Organization**
   - Scans dataset directory
   - Creates file inventory
   - Organizes by file type

3. **Data Analysis**
   - Performs EDA
   - Generates statistical insights
   - Creates summary reports
   - Saves findings to `insights.txt`

4. **Visualization**
   - Creates multiple visualization types
   - Saves as PNG files
   - Organizes in `visualizations` directory
   - Generates plot insights

5. **Report Generation**
   - Compiles all analyses
   - Incorporates visualizations
   - Creates structured PDF report
   - Saves in output directory

## Usage

To run the analysis pipeline:

```python
dataset_url = "https://huggingface.co/datasets/your-dataset"
initiate_sequential_workflow(dataset_url)
```

This will trigger the sequential workflow where each agent performs its designated tasks in order.

## Output Structure

```
dataset/
├── insights.txt           # EDA findings and statistical analysis
├── visualizations/        # Generated plots and charts
│   ├── plot1.png
│   ├── plot2.png
│   └── ...
├── plot_insights.txt      # Detailed analysis of visualizations
└── output/
    └── data_analysis_report.pdf  # Final compiled report
```

## Error Handling

The system includes robust error handling:
- File existence verification
- Exception catching and reporting
- Graceful failure handling
- Status updates and logging

## Extensibility

The system is designed to be modular and extensible:
- New agents can be added with specific roles
- Additional analysis steps can be incorporated
- Visualization types can be expanded
- Report formats can be customized

## Notes

- Ensure all dependencies are installed before running
- Verify API keys and configurations
- Check disk space for large datasets
- Monitor system resources during execution

## Contributing

Feel free to contribute to this project by:
- Adding new agent types
- Improving analysis methods
- Enhancing visualization capabilities
- Optimizing report generation

## License

This project is licensed under the MIT License - see the LICENSE file for details.
