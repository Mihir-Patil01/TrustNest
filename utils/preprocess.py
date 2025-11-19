import pandas as pd

# ----------------------------
# Load and clean flats dataset
# ----------------------------
def load_data(csv_path):
    df = pd.read_csv(csv_path)

    # Ensure required columns exist
    expected_cols = [
        'id', 'name', 'location', 'price', 'size', 'area',
        'rooms', 'number_of_bhk', 'amenities', 'lifestyle',
        'connectivity', 'utility', 'livability'
    ]
    for col in expected_cols:
        if col not in df.columns:
            df[col] = None

    # Convert numeric columns
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)
    df['size'] = pd.to_numeric(df['size'], errors='coerce').fillna(0)
    df['area'] = pd.to_numeric(df['area'], errors='coerce').fillna(0)
    df['rooms'] = pd.to_numeric(df['rooms'], errors='coerce').fillna(0).astype(int)
    df['number_of_bhk'] = pd.to_numeric(df['number_of_bhk'], errors='coerce').fillna(0).astype(int)
    df['livability'] = pd.to_numeric(df['livability'], errors='coerce').fillna(0)

    # Fill string columns
    str_cols = ['name', 'location', 'amenities', 'lifestyle', 'connectivity', 'utility']
    for col in str_cols:
        df[col] = df[col].fillna('').astype(str)

    return df


# ----------------------------
# Filter flats by given criteria
# ----------------------------
def filter_flats(df, filters: dict):
    df2 = df.copy()

    if filters.get('location'):
        loc = filters['location'].strip().lower()
        df2 = df2[df2['location'].str.lower().str.contains(loc, na=False)]

    if filters.get('budget_min') is not None:
        df2 = df2[df2['price'] >= float(filters['budget_min'])]

    if filters.get('budget_max') is not None:
        df2 = df2[df2['price'] <= float(filters['budget_max'])]

    if filters.get('rooms') is not None:
        try:
            r = int(filters['rooms'])
            df2 = df2[df2['rooms'] == r]
        except:
            pass

    if filters.get('number_of_bhk') is not None:
        try:
            bhk = int(filters['number_of_bhk'])
            df2 = df2[df2['number_of_bhk'] == bhk]
        except:
            pass

    if filters.get('lifestyle'):
        lf = filters['lifestyle'].strip().lower()
        df2 = df2[df2['lifestyle'].str.lower().str.contains(lf, na=False)]

    if filters.get('connectivity'):
        conn = filters['connectivity'].strip().lower()
        df2 = df2[df2['connectivity'].str.lower().str.contains(conn, na=False)]

    if filters.get('utility'):
        util = filters['utility'].strip().lower()
        df2 = df2[df2['utility'].str.lower().str.contains(util, na=False)]

    df2 = df2.sort_values(by=['livability', 'price'], ascending=[False, True])

    return df2


# ----------------------------
# Get flat by its unique ID
# ----------------------------
def get_flat_by_id(df, fid):
    fid = int(fid)
    rows = df[df['id'] == fid]
    if rows.empty:
        return None
    return rows.iloc[0].to_dict()
