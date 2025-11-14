from fastapi import FastAPI
from fastapi.responses import JSONResponse
import geopandas as gpd
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Update the file path to point to the GeoJSON file

p = Path(__file__).parent.parent.parent.parent
GEOJSON_PATH = p / "data/data_pmr.geojson"


# Serve the frontend
app.mount("/frontend", StaticFiles(directory="resultats/repository/geoparquet_app", html=True), name="frontend")

def load_geojson():
    # Load the GeoJSON file using GeoPandas
    gdf = gpd.read_file(GEOJSON_PATH)
    return gdf.to_crs(epsg=4326).to_json()

@app.get("/data")
async def get_geojson_data():
    try:
        geojson_data = load_geojson()
        return JSONResponse(content=geojson_data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)