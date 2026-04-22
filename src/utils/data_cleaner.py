
        
import pandas as pd
from abc import ABC, abstractmethod

# Define an abstract class for Data Cleaner
class DataCleaner(ABC):
    @abstractmethod
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Abstract method to clean the given DataFrame."""
        pass        

# Implement a concrete class for Data Cleaning
class AudibleDataCleaner(DataCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Cleans the Audible dataset."""
        """Cleans the Audible dataset by handling missing values and duplicates."""
        # Handle missing values (example: fill with median or drop)
        #df = df.fillna(df.median(numeric_only=True))  # Fill numeric columns with median
        #df = df.dropna()  # Drop any remaining rows with missing values

        # Remove duplicates
        df = df.drop_duplicates()

        # Strip whitespace from all string columns
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.strip()
        #Enforce the correct data types

        # Convert releasedate to datetime. Using mixed format to handle different date formats (Jan 01, 2020, 01/01/2020, etc), coerce errors to NaT
        df["releasedate"] = pd.to_datetime(df["releasedate"], format="mixed", errors="coerce")

        # Convert time to minutes and drop original time column
        df["minutes"] = (
            df["time"]
            .str.extract(r"(?:(\d+)\s*hr[s]?)?\s*(?:and)?\s*(\d+)\s*min")
            .astype(float)
            .fillna(0)
            .pipe(lambda x: x[0] * 60 + x[1])
        )
        df = df.drop(columns=["time"])

        # Standardize language to lowercase
        df["language"] = df["language"].str.lower()

        # Clean narrator and author columns
        df["narrator"] = df["narrator"].str.replace(r"^Narrated\s*by:\s*", "", regex=True)
        df["narrator"] = df["narrator"].str.replace(r"(?<=[a-z])(?=[A-Z])", " ", regex=True)
        df["author"] = df["author"].str.replace(r"^Written\s*by:\s*", "", regex=True)
        df["author"] = df["author"].str.replace(r"(?<=[a-z])(?=[A-Z])", " ", regex=True)

        # Convert price to numeric, fill na to0
        df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)

        # Extract rating and rating_count from stars column
        df[["rating", "rating_count"]] = df["stars"].str.extract(r"(\d+\.?\d*)\s*out of 5 stars\s*([\d,]+)")
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
        df["rating_count"] = pd.to_numeric(df["rating_count"], errors="coerce").fillna(0)
        df = df.drop(columns=["stars"])

        # Reset index
        df = df.reset_index(drop=True)

        return df


# Factory to create DataCleaners
class DataCleanerFactory:
    @staticmethod
    def get_data_cleaner(cleaner_type: str) -> DataCleaner:
        """Returns the appropriate DataCleaner based on type."""
        if cleaner_type == "audible":
            return AudibleDataCleaner()
        else:
            raise ValueError(f"No cleaner available for type: {cleaner_type}")