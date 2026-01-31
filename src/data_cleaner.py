"""
E-Commerce Data Cleaning Pipeline
Author: Your Name
Description: Clean and prepare e-commerce data for analysis

Functions:
1. clean_column_names() - Standardize column names
2. handle_missing_values() - Handle null values
3. normalize_text_columns() - Normalize text data
4. remove_invalid_data() - Remove invalid records
5. remove_duplicates() - Remove duplicate rows
"""

import pandas as pd
import numpy as np


# ============================================================================
# FUNCTION 1: CLEAN COLUMN NAMES
# ============================================================================

def clean_column_names(df):
    """Clean column names: lowercase, replace spaces with underscores"""
    print("\n🔧 Cleaning column names...")
    
    original_cols = df.columns.tolist()
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    print(f"   Original: {original_cols[:3]}...")
    print(f"   Cleaned:  {df.columns.tolist()[:3]}...")
    print("✅ Column names cleaned\n")
    
    return df


# ============================================================================
# FUNCTION 2: HANDLE MISSING VALUES
# ============================================================================

def handle_missing_values(df):
    """Handle missing values based on column type"""
    print("\n🔍 Handling missing values...")
    
    initial_rows = len(df)
    
    # Numerical columns - fill with median
    numerical_cols = ['price', 'quantity', 'customer_rating']
    
    for col in numerical_cols:
        if col in df.columns:
            missing_count = df[col].isnull().sum()
            
            if missing_count > 0:
                median_value = df[col].median()
                df[col] = df[col].fillna(median_value)
                
                print(f"   ✓ {col}: Filled {missing_count} nulls with median ({median_value:.2f})")
    
    # Category - fill with mode
    if 'category' in df.columns and df['category'].isnull().sum() > 0:
        missing_count = df['category'].isnull().sum()
        mode_value = df['category'].mode()[0]
        df['category'] = df['category'].fillna(mode_value)
        
        print(f"   ✓ category: Filled {missing_count} nulls with mode ('{mode_value}')")
    
    # Customer name - fill with 'Unknown Customer'
    if 'customer_name' in df.columns and df['customer_name'].isnull().sum() > 0:
        missing_count = df['customer_name'].isnull().sum()
        df['customer_name'] = df['customer_name'].fillna('Unknown Customer')
        
        print(f"   ✓ customer_name: Filled {missing_count} nulls with 'Unknown Customer'")
    
    # Email - drop rows (critical field)
    if 'email' in df.columns:
        email_nulls = df['email'].isnull().sum()
        
        if email_nulls > 0:
            df = df.dropna(subset=['email'])
            print(f"   ✓ email: Dropped {email_nulls} rows (email is critical)")
    
    # Payment status - fill with 'Unknown'
    if 'payment_status' in df.columns and df['payment_status'].isnull().sum() > 0:
        missing_count = df['payment_status'].isnull().sum()
        df['payment_status'] = df['payment_status'].fillna('Unknown')
        
        print(f"   ✓ payment_status: Filled {missing_count} nulls with 'Unknown'")
    
    # Order date - drop rows (critical field)
    if 'order_date' in df.columns and df['order_date'].isnull().sum() > 0:
        missing_count = df['order_date'].isnull().sum()
        df = df.dropna(subset=['order_date'])
        print(f"   ✓ order_date: Dropped {missing_count} rows (date is critical)")
    
    final_rows = len(df)
    rows_dropped = initial_rows - final_rows
    
    print(f"\n   📊 Rows before: {initial_rows}")
    print(f"   📊 Rows after:  {final_rows}")
    print(f"   📊 Rows dropped: {rows_dropped}")
    print("✅ Missing values handled\n")
    
    return df


# ============================================================================
# FUNCTION 3: NORMALIZE TEXT DATA
# ============================================================================

def normalize_text_columns(df):
    """Normalize text data: remove extra spaces, standardize case"""
    print("\n🔤 Normalizing text columns...")
    
    # Customer name - Title case
    if 'customer_name' in df.columns:
        df['customer_name'] = df['customer_name'].str.strip().str.title()
        print(f"   ✓ customer_name: Stripped spaces + Title case")
    
    # Email - lowercase
    if 'email' in df.columns:
        df['email'] = df['email'].str.strip().str.lower()
        print(f"   ✓ email: Stripped spaces + Lowercase")
    
    # Category - lowercase
    if 'category' in df.columns:
        before_unique = df['category'].nunique()
        df['category'] = df['category'].str.strip().str.lower()
        after_unique = df['category'].nunique()
        
        print(f"   ✓ category: Stripped spaces + Lowercase")
        print(f"      Before: {before_unique} unique → After: {after_unique} unique")
    
    # Payment status - lowercase
    if 'payment_status' in df.columns:
        df['payment_status'] = df['payment_status'].str.strip().str.lower()
        print(f"   ✓ payment_status: Stripped spaces + Lowercase")
    
    print("✅ Text normalization complete\n")
    return df


# ============================================================================
# FUNCTION 4: REMOVE INVALID DATA
# ============================================================================

def remove_invalid_data(df):
    """
    Remove invalid data
    
    Rules:
    - Price must be > 0
    - Quantity must be > 0
    - Rating must be 1-5
    - Email must contain '@'
    """
    print("\n❌ Removing invalid data...")
    
    initial_rows = len(df)
    
    # Invalid prices
    if 'price' in df.columns:
        invalid_price = (df['price'] <= 0).sum()
        
        if invalid_price > 0:
            print(f"   ⚠️  Found {invalid_price} rows with price <= 0")
            df = df[df['price'] > 0]
            print(f"   ✓ Removed {invalid_price} rows")
    
    # Invalid quantities
    if 'quantity' in df.columns:
        invalid_qty = (df['quantity'] <= 0).sum()
        
        if invalid_qty > 0:
            print(f"   ⚠️  Found {invalid_qty} rows with quantity <= 0")
            df = df[df['quantity'] > 0]
            print(f"   ✓ Removed {invalid_qty} rows")
    
    # Invalid ratings
    if 'customer_rating' in df.columns:
        invalid_rating = ((df['customer_rating'] < 1) | (df['customer_rating'] > 5)).sum()
        
        if invalid_rating > 0:
            print(f"   ⚠️  Found {invalid_rating} rows with rating not in 1-5")
            df = df[(df['customer_rating'] >= 1) & (df['customer_rating'] <= 5)]
            print(f"   ✓ Removed {invalid_rating} rows")
    
    # Invalid emails
    if 'email' in df.columns:
        invalid_email = (~df['email'].str.contains('@', na=False)).sum()
        
        if invalid_email > 0:
            print(f"   ⚠️  Found {invalid_email} rows with invalid email")
            df = df[df['email'].str.contains('@', na=False)]
            print(f"   ✓ Removed {invalid_email} rows")
    
    # Outlier detection (info only)
    if 'price' in df.columns:
        outlier_threshold = df['price'].quantile(0.99)
        outliers = (df['price'] > outlier_threshold).sum()
        
        if outliers > 0:
            print(f"\n   💡 {outliers} outliers detected (price > ${outlier_threshold:.2f})")
            print(f"      Keeping them (might be valid)")
    
    final_rows = len(df)
    rows_removed = initial_rows - final_rows
    
    print(f"\n   📊 Rows before: {initial_rows}")
    print(f"   📊 Rows after:  {final_rows}")
    print(f"   📊 Rows removed: {rows_removed}")
    
    print("✅ Invalid data removed\n")
    return df


# ============================================================================
# FUNCTION 5: REMOVE DUPLICATES
# ============================================================================

def remove_duplicates(df):
    """
    Remove duplicate rows (keep first occurrence)
    
    Parameters:
        df (DataFrame): Input dataframe
    
    Returns:
        DataFrame: Dataframe without duplicates
    """
    print("\n🔄 Removing duplicate rows...")
    
    initial_rows = len(df)
    
    # Count duplicates
    duplicate_count = df.duplicated().sum()
    
    if duplicate_count > 0:
        print(f"   ⚠️  Found {duplicate_count} duplicate rows")
        
        # Show example
        print("\n   Example duplicate (first 2 occurrences):")
        duplicate_sample = df[df.duplicated(keep=False)].head(2)
        print(duplicate_sample[['order_id', 'customer_name', 'email', 'price']].to_string(index=False))
        
        # Remove duplicates
        df = df.drop_duplicates(keep='first')
        
        print(f"\n   ✓ Removed {duplicate_count} rows (kept first occurrence)")
    else:
        print("   ✓ No duplicates found")
    
    final_rows = len(df)
    
    print(f"\n   📊 Rows before: {initial_rows}")
    print(f"   📊 Rows after:  {final_rows}")
    
    print("✅ Duplicates removed\n")
    return df


# ============================================================================
# MAIN PIPELINE: Clean the data
# ============================================================================

def clean_data_pipeline(input_path, output_path):
    """
    Complete data cleaning pipeline
    
    Parameters:
        input_path (str): Path to raw CSV file
        output_path (str): Path to save cleaned CSV file
    
    Returns:
        DataFrame: Cleaned dataframe
    """
    print("\n" + "=" * 70)
    print("🚀 STARTING DATA CLEANING PIPELINE")
    print("=" * 70)
    
    # Load data
    print(f"\n📂 Loading data from: {input_path}")
    df = pd.read_csv(input_path)
    print(f"   Initial shape: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Run all cleaning steps
    df = clean_column_names(df)
    df = handle_missing_values(df)
    df = normalize_text_columns(df)
    df = remove_invalid_data(df)
    df = remove_duplicates(df)
    
    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"\n💾 Cleaned data saved to: {output_path}")
    print(f"   Final shape: {df.shape[0]} rows, {df.shape[1]} columns")
    
    print("\n" + "=" * 70)
    print("✅ PIPELINE COMPLETE!")
    print("=" * 70)
    
    return df


# ============================================================================
# MAIN: TEST ALL FUNCTIONS
# ============================================================================

if __name__ == "__main__":
    
    print("=" * 70)
    print("🧪 TESTING DATA CLEANING PIPELINE")
    print("=" * 70)
    
    # Load data
    print("\n📂 Loading raw data...")
    df = pd.read_csv('data/raw/ecommerce_raw_data.csv')
    
    print(f"   Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"   Missing values: {df.isnull().sum().sum()}")
    print(f"   Duplicates: {df.duplicated().sum()}")
    
    # TEST 1
    print("\n" + "-" * 70)
    print("TEST 1: CLEAN COLUMN NAMES")
    print("-" * 70)
    df = clean_column_names(df)
    
    # TEST 2
    print("\n" + "-" * 70)
    print("TEST 2: HANDLE MISSING VALUES")
    print("-" * 70)
    df = handle_missing_values(df)
    
    # TEST 3
    print("\n" + "-" * 70)
    print("TEST 3: NORMALIZE TEXT DATA")
    print("-" * 70)
    df = normalize_text_columns(df)
    
    # TEST 4
    print("\n" + "-" * 70)
    print("TEST 4: REMOVE INVALID DATA")
    print("-" * 70)
    df = remove_invalid_data(df)
    
    # TEST 5
    print("\n" + "-" * 70)
    print("TEST 5: REMOVE DUPLICATES")
    print("-" * 70)
    print(f"\nBEFORE: {len(df)} rows")
    print(f"   Duplicates: {df.duplicated().sum()}")
    
    df = remove_duplicates(df)
    
    print(f"\nAFTER: {len(df)} rows")
    print(f"   Duplicates: {df.duplicated().sum()} ✅")
    
    # FINAL SUMMARY
    print("\n" + "=" * 70)
    print("✅ ALL TESTS COMPLETE!")
    print("=" * 70)
    print(f"\n📊 Final dataset:")
    print(f"   Rows: {df.shape[0]}")
    print(f"   Columns: {df.shape[1]}")
    print(f"   Missing values: {df.isnull().sum().sum()}")
    print(f"   Duplicates: {df.duplicated().sum()}")
    print(f"   Invalid data: 0")
    
    # Save cleaned data
    print("\n💾 Saving cleaned data...")
    df.to_csv('data/cleaned/ecommerce_cleaned_data.csv', index=False)
    print("   Saved to: data/cleaned/ecommerce_cleaned_data.csv")