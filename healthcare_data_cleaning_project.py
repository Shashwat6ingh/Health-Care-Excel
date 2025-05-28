
import pandas as pd

def load_data(file_path):
    """Load healthcare provider data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Clean the provider data: remove duplicates, handle missing values."""
    # Remove duplicate records
    df_cleaned = df.drop_duplicates()

    # Fill missing emails and contact numbers with 'Unknown'
    df_cleaned['Email'].fillna('unknown@domain.com', inplace=True)
    df_cleaned['Contact Number'].fillna('Not Provided', inplace=True)

    print("Data cleaning completed.")
    return df_cleaned

def save_cleaned_data(df, output_path):
    """Save the cleaned data to a new CSV file."""
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to: {output_path}")
    except Exception as e:
        print(f"Error saving cleaned data: {e}")

if __name__ == "__main__":
    input_file = "Healthcare_Provider_Data.csv"  # Replace with your actual file path
    output_file = "Cleaned_Healthcare_Provider_Data.csv"

    df = load_data(input_file)
    if df is not None:
        cleaned_df = clean_data(df)
        save_cleaned_data(cleaned_df, output_file)
