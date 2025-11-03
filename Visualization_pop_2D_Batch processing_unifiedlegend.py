import os, glob, numpy as np, geopandas as gpd, pandas as pd
import matplotlib.pyplot as plt, matplotlib.colors as mcolors

POINT_SIZE = 10
CMAP_STEADY = 'plasma_r'       # 粉-蓝
CMAP_MODEL  = 'plasma_r'   # 黄-紫(反向)

def _plot(ax, df, x, y, v, norm, cmap):
    df = df[df[v] >= 1]
    ax.scatter(df[x], df[y], c=df[v], cmap=cmap, norm=norm,
               s=POINT_SIZE, alpha=.7, edgecolors='face')

def _axes(ax, norm, cmap, mlat):
    plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax,
                 label='Population')
    ax.set_xlabel('Longitude'); ax.set_ylabel('Latitude')
    ax.set_aspect(1 / np.cos(np.deg2rad(mlat)))
    ax.grid(ls='--', lw=.3, alpha=.4)
    for s in ax.spines.values(): s.set_visible(True), s.set_linewidth(.6)

def steady_plot(steady_csv, centroid_csv, boundary, out_png, norm):
    df = pd.read_csv(steady_csv).merge(pd.read_csv(centroid_csv), on='new_id')
    bnd = gpd.read_file(boundary).to_crs(epsg=4326)
    fig, ax = plt.subplots(figsize=(10, 8))
    bnd.plot(ax=ax, facecolor='none', edgecolor='black', linewidth=.1)
    _plot(ax, df, 'longitude', 'latitude', 'steady_pop', norm, CMAP_STEADY)
    _axes(ax, norm, CMAP_STEADY, df['latitude'].mean())
    plt.savefig(out_png, dpi=300, bbox_inches='tight'); plt.close()

def model_plot(grid_geo, boundary, nodes_csv, out_png, norm):
    gdf  = gpd.read_file(grid_geo).to_crs(epsg=4326)
    bnd  = gpd.read_file(boundary).to_crs(epsg=4326)
    nodes = pd.read_csv(nodes_csv).astype({'new_id': str})
    df = gdf[['new_id', 'geometry']].astype({'new_id': str}).merge(nodes, on='new_id')
    df['lon'] = df.geometry.centroid.x; df['lat'] = df.geometry.centroid.y
    fig, ax = plt.subplots(figsize=(10, 8))
    bnd.plot(ax=ax, facecolor='none', edgecolor='black', linewidth=.1)
    _plot(ax, df, 'lon', 'lat', 'population', norm, CMAP_MODEL)
    _axes(ax, norm, CMAP_MODEL, df['lat'].mean())
    plt.savefig(out_png, dpi=300, bbox_inches='tight'); plt.close()

def main(city='BJ', year='2024'):
    data_dir  = f'Data&Result_{city}\\Data'
    base_dir  = f'Data&Result_{city}\\Result'
    steady    = f'{data_dir}/{year}pop_steadystate.csv'
    centroids = f'{data_dir}/centroidsv2.csv'
    boundary  = f'{data_dir}/{city}_cbg.geojson'
    grid_geo  = f'{data_dir}/grid_with_pois.geojson'

    vmax = pd.read_csv(steady)['steady_pop'].max()
    norm = mcolors.LogNorm(vmin=1, vmax=vmax)

    steady_plot(steady, centroids, boundary,
                os.path.join(base_dir, 'spatial_steady_state.png'), norm)

    for d in [f.path for f in os.scandir(base_dir) if f.is_dir()]:
        for csv in glob.glob(os.path.join(d, 'output_nodes*.csv')):
            png = os.path.join(d, f"spatial_{os.path.splitext(os.path.basename(csv))[0]}.png")
            model_plot(grid_geo, boundary, csv, png, norm)

if __name__ == '__main__':
    main()
