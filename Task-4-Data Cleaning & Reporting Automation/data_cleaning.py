import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set plotting style for professional look
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Liberation Sans']

def automate_data_cleaning():
    print("==================================================")
    print("      STUDENT PERFORMANCE DATA CLEANING PIPELINE  ")
    print("==================================================")
    
    # 1. Load the Students Performance Dataset
    csv_filename = 'Student_Performance.csv'
    if not os.path.exists(csv_filename):
        print(f"Error: Raw data file '{csv_filename}' not found in the current directory.")
        return
        
    print(f"\n[Step 1] Loading dataset '{csv_filename}'...")
    df = pd.read_csv(csv_filename)
    total_raw_records = len(df)
    print(f"Dataset loaded successfully. Total raw records: {total_raw_records}")
    
    # 2. Display the first 5 rows and dataset information
    print("\n[Step 2] Displaying the first 5 rows of the dataset:")
    print(df.head())
    
    print("\nDisplaying dataset information (dtypes and memory usage):")
    print(df.info())
    
    # 3. Check for missing values
    print("\n[Step 3] Checking for missing values in all columns:")
    missing_values = df.isnull().sum()
    print(missing_values)
    
    # 4. Handle missing values (if they exist)
    print("\n[Step 4] Handling missing values (if any)...")
    has_missing = missing_values.sum() > 0
    if has_missing:
        print("Missing values detected. Initiating data imputation:")
        for col in df.columns:
            col_missing = df[col].isnull().sum()
            if col_missing > 0:
                print(f" - Column '{col}' has {col_missing} missing values.")
                # Impute numeric columns with median, categorical columns with mode
                if df[col].dtype in ['float64', 'int64']:
                    median_val = df[col].median()
                    df[col] = df[col].fillna(median_val)
                    print(f"   Imputed missing values in '{col}' with median: {median_val}")
                else:
                    mode_val = df[col].mode()[0]
                    df[col] = df[col].fillna(mode_val)
                    print(f"   Imputed missing values in '{col}' with mode: '{mode_val}'")
    else:
        print("No missing values were found. The dataset is already complete.")
        
    # 5. Remove duplicate records
    print("\n[Step 5] Checking and removing duplicate records...")
    duplicate_count = df.duplicated().sum()
    print(f"Number of duplicate records found: {duplicate_count}")
    if duplicate_count > 0:
        df = df.drop_duplicates()
        print(f"Successfully removed {duplicate_count} duplicate records.")
        print(f"Remaining records after removing duplicates: {len(df)}")
    else:
        print("No duplicate records found.")
        
    # 6. Remove leading and trailing spaces from text columns
    print("\n[Step 6] Removing leading and trailing whitespace from text columns...")
    text_columns = df.select_dtypes(include=['object']).columns
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()
    print(f"Stripped leading/trailing spaces from columns: {list(text_columns)}")
    
    # 7. Standardize text values (Title Case / Proper Case)
    print("\n[Step 7] Standardizing text values to Title Case...")
    for col in text_columns:
        df[col] = df[col].str.title()
    # Explicitly fix 'PhD' capitalization for professional formatting
    if 'parent_education' in df.columns:
        df['parent_education'] = df['parent_education'].replace({'Phd': 'PhD'})
    print("Casing standardized successfully (e.g., 'male' -> 'Male', 'high school' -> 'High School', 'Phd' -> 'PhD').")
    
    # 8. Verify and correct data types
    print("\n[Step 8] Verifying and correcting data types...")
    # Student ID should be integer
    df['student_id'] = df['student_id'].astype(int)
    # Age should be integer
    df['age'] = df['age'].astype(int)
    # Study hours and attendance percentage should be float
    df['study_hours'] = df['study_hours'].astype(float)
    df['attendance_percentage'] = df['attendance_percentage'].astype(float)
    # Score columns should be float
    score_cols = ['math_score', 'science_score', 'english_score', 'overall_score']
    for col in score_cols:
        df[col] = df[col].astype(float)
    print("Data types verified and updated.")
    print(df.dtypes)
    
    # 9. Generate summary statistics
    print("\n[Step 9] Generating summary statistics for numerical columns:")
    summary_stats = df.describe()
    print(summary_stats)
    
    # 10. Create Visualizations
    print("\n[Step 10] Generating visualizations...")
    output_charts = []
    
    # Color palette
    primary_color = '#1E3D59'   # Sleek Slate Blue
    secondary_color = '#17B890' # Fresh Teal
    accent_color = '#FF6B6B'    # Warm Coral
    neutral_dark = '#333333'
    
    # Plot 1: Distribution of Math Scores
    plt.figure(figsize=(8, 5))
    plt.hist(df['math_score'], bins=20, color=secondary_color, edgecolor=primary_color, alpha=0.85)
    plt.title('Distribution of Math Scores', fontsize=14, fontweight='bold', pad=15, color=primary_color)
    plt.xlabel('Math Score', fontsize=12, labelpad=10, color=neutral_dark)
    plt.ylabel('Frequency', fontsize=12, labelpad=10, color=neutral_dark)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    chart1_path = 'math_score_distribution.png'
    plt.savefig(chart1_path, dpi=150)
    plt.close()
    output_charts.append(chart1_path)
    print(f" - Saved distribution chart as '{chart1_path}'")
    
    # Plot 2: Average Scores by Gender
    gender_grouped = df.groupby('gender')[['math_score', 'science_score', 'english_score']].mean()
    plt.figure(figsize=(9, 5.5))
    x = np.arange(len(gender_grouped.index))
    width = 0.25
    
    plt.bar(x - width, gender_grouped['math_score'], width, label='Math Score', color='#1E3D59')
    plt.bar(x, gender_grouped['science_score'], width, label='Science Score', color='#17B890')
    plt.bar(x + width, gender_grouped['english_score'], width, label='English Score', color='#FF6B6B')
    
    plt.title('Average Test Scores by Gender', fontsize=14, fontweight='bold', pad=15, color=primary_color)
    plt.xlabel('Gender', fontsize=12, labelpad=10, color=neutral_dark)
    plt.ylabel('Average Score', fontsize=12, labelpad=10, color=neutral_dark)
    plt.xticks(x, gender_grouped.index, fontsize=11)
    plt.legend(frameon=True, facecolor='white', edgecolor='none')
    plt.ylim(0, 105)
    
    # Add values on top of bars
    for i, gender in enumerate(gender_grouped.index):
        for j, col in enumerate(['math_score', 'science_score', 'english_score']):
            score = gender_grouped.loc[gender, col]
            plt.text(i + (j - 1) * width, score + 1.5, f"{score:.1f}", ha='center', va='bottom', fontsize=9, fontweight='bold')
            
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    chart2_path = 'avg_scores_by_gender.png'
    plt.savefig(chart2_path, dpi=150)
    plt.close()
    output_charts.append(chart2_path)
    print(f" - Saved average scores by gender chart as '{chart2_path}'")
    
    # Plot 3: Average Overall Score by Parental Education
    # Define logical order for education levels
    edu_order = ['No Formal', 'High School', 'Diploma', 'Graduate', 'Post Graduate', 'PhD']
    # Filter the education values to group them in order
    edu_grouped = df.groupby('parent_education')['overall_score'].mean().reindex(edu_order)
    
    plt.figure(figsize=(9, 5))
    bars = plt.barh(edu_grouped.index, edu_grouped.values, color='#17B890', edgecolor='#1E3D59', height=0.6, alpha=0.9)
    plt.title('Average Overall Score by Parental Education Level', fontsize=14, fontweight='bold', pad=15, color=primary_color)
    plt.xlabel('Average Overall Score', fontsize=12, labelpad=10, color=neutral_dark)
    plt.ylabel('Parental Education Level', fontsize=12, labelpad=10, color=neutral_dark)
    plt.xlim(0, 105)
    
    # Add values to the bars
    for bar in bars:
        width_val = bar.get_width()
        plt.text(width_val + 1.5, bar.get_y() + bar.get_height()/2, f"{width_val:.1f}", 
                 va='center', ha='left', fontsize=10, fontweight='bold', color=neutral_dark)
                 
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    chart3_path = 'avg_scores_by_parent_education.png'
    plt.savefig(chart3_path, dpi=150)
    plt.close()
    output_charts.append(chart3_path)
    print(f" - Saved average scores by parent education chart as '{chart3_path}'")
    
    # 11. Save the cleaned dataset as Cleaned_Students_Performance.xlsx
    excel_filename = 'Cleaned_Students_Performance.xlsx'
    print(f"\n[Step 11] Saving cleaned dataset as Excel spreadsheet '{excel_filename}'...")
    df.to_excel(excel_filename, index=False, engine='openpyxl')
    print(f"Cleaned dataset saved successfully. Shape: {df.shape}")
    
    # 12. Generate a text report summarizing the data cleaning pipeline
    report_filename = 'data_cleaning_report.txt'
    print(f"\n[Step 12] Generating text report '{report_filename}'...")
    
    with open(report_filename, 'w') as report:
        report.write("======================================================================\n")
        report.write("          DATA CLEANING & REPORTING AUTOMATION REPORT\n")
        report.write("======================================================================\n\n")
        report.write("1. DATA SUMMARY METRICS\n")
        report.write("-----------------------\n")
        report.write(f"Total Raw Records Loaded:     {total_raw_records}\n")
        report.write(f"Duplicate Records Removed:    {duplicate_count}\n")
        report.write(f"Missing Values Checked:       {missing_values.sum()} found in raw file\n")
        report.write(f"Missing Values Imputed:       {'Yes (mode/median)' if has_missing else 'No missing values detected (0)'}\n")
        report.write(f"Total Cleaned Records Saved:  {len(df)}\n\n")
        
        report.write("2. COLUMN DETAILS & DATA TYPES\n")
        report.write("------------------------------\n")
        for col, dtype in zip(df.columns, df.dtypes):
            report.write(f" - {col:<25} : {str(dtype)}\n")
        report.write("\n")
        
        report.write("3. SUMMARY STATISTICS FOR SCORES\n")
        report.write("--------------------------------\n")
        report.write(summary_stats.to_string())
        report.write("\n\n")
        
        report.write("4. LOGICAL CATEGORY SUMMARY\n")
        report.write("---------------------------\n")
        report.write("Records by Gender:\n")
        report.write(df['gender'].value_counts().to_string())
        report.write("\n\n")
        report.write("Records by School Type:\n")
        report.write(df['school_type'].value_counts().to_string())
        report.write("\n\n")
        report.write("Records by Parental Education:\n")
        report.write(df['parent_education'].value_counts().to_string())
        report.write("\n\n")
        report.write("Records by Final Grade:\n")
        report.write(df['final_grade'].value_counts().to_string())
        report.write("\n\n")
        report.write("======================================================================\n")
        report.write("Report generated successfully by Data Cleaning Automation Pipeline.\n")
        
    print(f"Data cleaning report written to '{report_filename}'")
    print("\n==================================================")
    print("      DATA CLEANING PROCESS COMPLETED SUCCESSFULLY ")
    print("==================================================")

if __name__ == "__main__":
    automate_data_cleaning()
