import geopandas as gpd
from pathlib import Path

p = Path(__file__).parent / "../data"
p = p.resolve()
po = p / "../data_out"
po = po.resolve()

def load_gare_idfm():
    """Converts Rerentiel Gare IDFM to GeoJSON"""
    PATH = po / rer_gare_idfm.parquet
    


if __name__ == "__main__":
    print(str(p))
    print(str(po))