"""
Author: Moritz Staaden
Datum: 12.01.2026

This script is used to determine the important index per substation, which is equivalent to criticality.
Criticality represents another parameter of the risk index,
in this research, aims to assess cascade effects during heavy rainfall events.
Technical parameters of the substation and their relevance to the power grid are taken into account.
This represents the direct effects on the power supply.
The individual parameters were weighted using the Analytic Hierarchy Process
(AHP) method according to Saaty (1987) by comparing them in pairs.

Five parameters are used:
 1. Leistung Bezug
 2. Netzknotenbewertung (NKB)
 3. Versorgte Einwohner
 4. Versorgung Gewerbe
 5. Versorgung kritische Infrastruktur

Formula:
II = Σ(S_i * W_i) / Σ(S_max,i * W_i)
II normalized = (II - II_min) / (II_max - II_min)
"""

import pandas as pd

def rate_leistung_bezug(leistung):
    """
    Rates Leistung Bezug
    < 83,8 kVA: 1 (low)
    83,8-185,53 kVA: 2 (medium)
    >=185,53 kVA: 3 (high)
    """
    if pd.isna(leistung):
        leistung = 0
    
    if leistung < 83.80:
        return 1
    elif leistung < 185.53:
        return 2
    else:
        return 3


def rate_einwohner(einwohner):
    """
    Rates Anzahl versorgte Einwohner
    < 130: 1 (low)
    130-273: 2 (medium)
    >= 274: 3 (high)
    """
    if pd.isna(einwohner):
        einwohner = 0
    
    if einwohner < 130:
        return 1
    elif einwohner < 274:
        return 2
    else:
        return 3


def rate_nkb(nkb):
    """
    Rates NKB (Netzknotenbewertung)
    0: 1 (low)
    < 0,5: 2 (medium)
    >= 0,5: 3 (high)
    """
    if pd.isna(nkb):
        nkb = 0
    
    if nkb == 0:
        return 1
    elif nkb < 0.5:
        return 2
    else:
        return 3


def rate_infrastruktur(infrastruktur):
    """
    Rates kritische Infrastruktur
    0: 1 (low)
    < 2: 2 (medium)
    >= 2: 3 (high)
    """
    if pd.isna(infrastruktur):
        infrastruktur = 0
    
    if infrastruktur == 0:
        return 1
    elif infrastruktur < 2:
        return 2
    else:
        return 3


def rate_gewerbe(gewerbe):
    """
    Rates Anzahl Gewerbe
    < 4: 1 (low)
    4-12: 2 (medium)
    >= 13: 3 (high)
    """
    if pd.isna(gewerbe):
        gewerbe = 0
    
    if gewerbe < 4:
        return 1
    elif gewerbe < 13:
        return 2
    else:
        return 3


def weighted_index(df, leistung='Übertragungsleistung Bezug', einwohner='Einwohner', nkb='NKB', infrastruktur='Infrastruktur', gewerbe='Gewerbe'):
    """
    Calculates the weighted index (II) and normalized index (II_N) for the given DataFrame.
    """
    
    # Weights for all criteria
    WEIGHTS = {
        'power_supply': 0.062,
        'residents': 0.250,
        'nkb': 0.118,
        'infrastruktur': 0.537,
        'commercial': 0.033
    }
    
    # Maximal score for each criterion
    S_MAX = 3
    
    # Calculate ratings for each criterion
    df['Leistung'] = df[leistung].apply(rate_leistung_bezug)
    df['Einwohner'] = df[einwohner].apply(rate_einwohner)
    df['NKB'] = df[nkb].apply(rate_nkb)
    df['Infrastruktur'] = df[infrastruktur].apply(rate_infrastruktur)
    df['Gewerbe'] = df[gewerbe].apply(rate_gewerbe)
    
    # Calculate weighted sum for numerator: Σ(S_i * W_i)
    df['counter'] = (
        df['Leistung'] * WEIGHTS['power_supply'] +
        df['Einwohner'] * WEIGHTS['residents'] +
        df['NKB'] * WEIGHTS['nkb'] +
        df['Infrastruktur'] * WEIGHTS['infrastruktur'] +
        df['Gewerbe'] * WEIGHTS['commercial']
    )
    
    # Calculate weighted sum for denominator: Σ(S_max,i * W_i)
    denominator = S_MAX * sum(WEIGHTS.values())
    
    # Calculate index II
    df['II'] = df['counter'] / denominator
    
    # Calculate normalized index II_N
    II_MAX = 1.0
    II_MIN = 1.0 / 3.0
    
    df['II_N'] = (df['II'] - II_MIN) / (II_MAX - II_MIN)
    
    # Clip values to the range [0, 1] to avoid rounding errors
    df['II_N'] = df['II_N'].clip(lower=0.0, upper=1.0)
       
    return df

def criticality():
    """
    Main function for loading data and calculating the index
    """

    csv_path = r"c:\Untersuchungsgebiet\criticality.csv"
    df = pd.read_csv(csv_path, sep=';', encoding='latin-1')
        
    # Calculate index
    df = weighted_index(df)
    
    # Remove intermediate columns before saving
    df = df.drop(columns=['counter', 'II'])
    
    # Save result back to the original CSV
    print(f"\nResults saved as new column in original file: {csv_path}")
    df.to_csv(csv_path, index=False, sep=';', encoding='latin-1')
    
# Execute the criticality function
criticality()