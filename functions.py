import numpy as np

def rolling_calculator(df, weeks):
    result_df = df.copy()

    stat_cols = result_df.select_dtypes(include=[np.number]).columns.tolist()
    if "GW" in stat_cols:
        stat_cols.remove("GW")

    # Sort by player name and then GW
    result_df = result_df.sort_values(['name', 'GW'])
    
    # Loop through each stat column and calculate rolling totals per player
    for col in stat_cols:
        result_df[f'{col}_last_{weeks}_games'] = (
            result_df.groupby('name')[col]
            .rolling(window=weeks, min_periods=1)
            .sum()
            .reset_index(level=0, drop=True)
        )
    
    return result_df, stat_cols