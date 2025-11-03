import geopandas as gpd
import pandas as pd
from itertools import combinations
from shapely.geometry import Point
from tqdm import tqdm

city = 'BJ'
path=f'Data&Result_{city}/Data'
df = pd.read_csv(f'{path}/centroidsv2.csv')
df['geometry'] = df.apply(lambda x: Point((x['longitude'], x['latitude'])), axis=1)

gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")

gdf = gdf.to_crs(epsg=32633)

edges = []
combs = list(combinations(range(len(gdf)), 2))
for i, j in tqdm(combs, desc="Calculating distances"):
    distance = gdf.geometry.iloc[i].distance(gdf.geometry.iloc[j])
    edges.append([df['new_id'].iloc[i], df['new_id'].iloc[j], distance])

edge_df = pd.DataFrame(edges, columns=['source_id', 'target_id', 'distance'])
edge_df.to_csv(f'{path}/distance.csv', index=False)  # unit：meter
