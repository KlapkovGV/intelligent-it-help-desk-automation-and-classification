import pandas as pd
import time
import os
from dotenv import load_dotenv

# Import custom modules from the src directory
from src.regex_filter import classify_by_regex
from src.llm_classifier import get_llm_classification

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def main():
    # Load the full dataset from Hugging Face
    print("Loading dataset...")
    df = pd.read_csv("hf://datasets/Console-AI/IT-helpdesk-synthetic-tickets/tickets.csv")

    # Keep only required columns
    df = df[['id', 'subject', 'description']]

    # Initialize the column for final classification results
    df['final_category'] = ''

    # Iterate through all rows in the dataframe
    for i, row in df.iterrows():
        description = row['description']
        
        print(f"Processing Message {i+1}/{len(df)}: {description[:50]}...")

        # Stage 1: Attempt classification using Regex
        regex_result = classify_by_regex(description)

        if regex_result == 'Ambiguous':
            # Stage 2: Route to LLM if Regex cannot determine the category
            print("  Regex: Ambiguous. Routing to LLM...")
            
            llm_result = get_llm_classification(description, API_KEY)
            df.at[i, 'final_category'] = llm_result
            
            print(f"  LLM Classification: {llm_result}")
            
            # API rate limit management: wait 13 seconds between requests
            print("  Waiting 13 seconds...")
            time.sleep(13)
        else:
            # Classification successful via Regex
            df.at[i, 'final_category'] = regex_result
            print(f"  Regex Classification: {regex_result}")
        
        print("-" * 20)

    # Export all processed data to a CSV file
    output_filename = "results.csv"
    df.to_csv(output_filename, index=False)

if __name__ == "__main__":
    main()
