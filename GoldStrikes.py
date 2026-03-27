import pandas as pd
import numpy as np


# =========================
# CORE PROCESS
# =========================
def process_file(input_source):
    # Accepts file path OR file-like object
    df = pd.read_csv(input_source, on_bad_lines='skip')

    # Parse Strike
    df[['Strike', 'Type']] = df['Strike'].astype(str).str.extract(r'([\d,\.]+)([CP])')
    df['Strike'] = df['Strike'].str.replace(',', '', regex=False).astype(float)

    # Clean numeric
    df['Open Int'] = pd.to_numeric(df['Open Int'], errors='coerce').fillna(0)
    df['Premium'] = pd.to_numeric(df['Premium'], errors='coerce').fillna(0)

    # Split Calls / Puts
    calls = df[df['Type'] == 'C'].copy()
    puts  = df[df['Type'] == 'P'].copy()

    calls = calls.rename(columns={
        'Open Int': 'Call_OInt',
        'Premium': 'Call_Premium'
    })

    puts = puts.rename(columns={
        'Open Int': 'Put_OInt',
        'Premium': 'Put_Premium'
    })

    merged = pd.merge(
        calls[['Strike', 'Call_OInt', 'Call_Premium']],
        puts[['Strike', 'Put_OInt', 'Put_Premium']],
        on='Strike',
        how='outer'
    ).fillna(0)

    # Metrics
    merged['Call_Exposure'] = merged['Call_OInt'] * merged['Call_Premium']
    merged['Put_Exposure'] = merged['Put_OInt'] * merged['Put_Premium']

    merged['Total_Exposure'] = merged['Call_Exposure'] + merged['Put_Exposure']

    merged['Dominance_Log'] = np.log(
        (merged['Call_Exposure'] + 1) /
        (merged['Put_Exposure'] + 1)
    )

    # Output format
    result = merged[['Strike', 'Total_Exposure', 'Dominance_Log']].copy()

    result['Strike'] = result['Strike'].round(2)
    result['Total_Exposure'] = result['Total_Exposure'].astype(int)
    result['Dominance_Log'] = result['Dominance_Log'].round(2)

    result = result.sort_values('Strike', ascending=False)

    return result


# =========================
# EXPORT (MT5 CSV)
# =========================
def to_csv_bytes(df):
    return df.to_csv(index=False).encode('utf-8')
