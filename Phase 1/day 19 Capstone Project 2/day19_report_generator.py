import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats
from exceptions import InvalidDataError


class ReportGenerator():
    def __init__(self, df):
        self.df = df
        self.output_dir = Path(__file__).parent / "reports"
        self.output_dir.mkdir(exist_ok=True)
        self.stats_log_file = self.output_dir / "skewness_stats.log"
        
        # Execute the pipeline
        self.df = self.clean_data(self.df)
        self.generate_histograms(self.df)
        self.log_skewness(self.df)
        self.report_generator(self.df)


    def clean_data(self, df):
        """
        Clean the DataFrame by auto-filling missing values with column mean.
        Only processes numeric columns.
        """
        try:
            df_cleaned = df.copy()
            numeric_columns = df_cleaned.select_dtypes(include=[np.number]).columns
            
            for col in numeric_columns:
                if df_cleaned[col].isnull().sum() > 0:
                    mean_value = df_cleaned[col].mean()
                    df_cleaned[col] = df_cleaned[col].fillna(mean_value)
                    logging.info(f"Filled missing values in '{col}' with mean: {mean_value}")
            
            logging.info("Data cleaning completed successfully.")
            return df_cleaned
            
        except Exception as e:
            logging.error(f"Error occurred while cleaning data: {e}")
            raise InvalidDataError(f"Data cleaning failed: {e}")


    def generate_histograms(self, df):
        """
        Generate and save .png histograms for every numeric column.
        """
        try:
            numeric_columns = df.select_dtypes(include=[np.number]).columns
            
            for col in numeric_columns:
                plt.figure(figsize=(10, 6))
                plt.hist(df[col], bins=20, edgecolor='black', alpha=0.7)
                plt.title(f"Histogram of {col}")
                plt.xlabel(col)
                plt.ylabel("Frequency")
                plt.grid(axis='y', alpha=0.3)
                
                # Save the histogram
                histogram_path = self.output_dir / f"histogram_{col}.png"
                plt.savefig(histogram_path, dpi=100, bbox_inches='tight')
                plt.close()
                
                logging.info(f"Histogram saved for '{col}' at {histogram_path}")
            
            logging.info("All histograms generated successfully.")
            
        except Exception as e:
            logging.error(f"Error occurred while generating histograms: {e}")
            raise


    def log_skewness(self, df):
        """
        Calculate and log the skewness of every column to a file.
        """
        try:
            with open(self.stats_log_file, 'w') as f:
                f.write("=" * 60 + "\n")
                f.write("SKEWNESS STATISTICS REPORT\n")
                f.write("=" * 60 + "\n\n")
                
                numeric_columns = df.select_dtypes(include=[np.number]).columns
                
                for col in numeric_columns:
                    skewness_value = stats.skew(df[col].dropna())
                    f.write(f"Column: {col}\n")
                    f.write(f"Skewness: {skewness_value:.4f}\n")
                    f.write("-" * 40 + "\n")
                    
                    logging.info(f"Skewness for '{col}': {skewness_value:.4f}")
                
                f.write("\n" + "=" * 60 + "\n")
                f.write("Report generation completed successfully.\n")
            
            logging.info(f"Skewness statistics logged to {self.stats_log_file}")
            
        except Exception as e:
            logging.error(f"Error occurred while logging skewness: {e}")
            raise


    def report_generator(self, df):
        """
        Generate and display a comprehensive report with summary statistics.
        """
        try:
            report = df.describe()
            print("\n" + "=" * 60)
            print("COMPREHENSIVE DATA REPORT")
            print("=" * 60)
            print("\nSummary Statistics:")
            print(report)
            print("=" * 60 + "\n")
            
            logging.info("Report generated successfully.")
            
        except Exception as e:
            logging.error(f"Error occurred while generating report: {e}")
        


    