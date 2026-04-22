#For main: ingest,clean, output the clean data

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.data_ingestor import DataIngestorFactory
from utils.data_cleaner import DataCleanerFactory

def main():
    #Ingest
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "Audible data.zip"))

    file_extension = os.path.splitext(file_path)[1]

    ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    df = ingestor.ingest(file_path)

    #check the shape and the head of the dataframe to ensure everythings reading correctly
    print(df.shape)
    print(df.head())

    #Clean
    cleaner = DataCleanerFactory.get_data_cleaner("audible")
    df_cleaned=cleaner.clean(df)
    #check the shape and the head of the cleaned dataframe to ensure everythings reading correctly
    print(df_cleaned.shape)
    print(df_cleaned.head())
    print(df_cleaned.dtypes)

    #Output
    #Output the cleaned data to a new CSV file
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "processed"))
    os.makedirs(output_dir, exist_ok=True)  # creates the folder if it doesn't exist

    output_path = os.path.join(output_dir, "audible_cleaned.csv")
    df_cleaned.to_csv(output_path, index=False)

    print(f"Cleaned data saved to: {output_path}")


if __name__ == "__main__":
    main()