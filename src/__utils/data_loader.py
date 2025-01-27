def load_data():
    """
    Загружает данные о странах и морях из репозиториев Natural Earth.
    Возвращает два GeoDataFrame: world (страны) и marine_polys (моря/океаны).
    """
    url_countries = (
        "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/"
        "master/geojson/ne_50m_admin_0_countries.geojson"
    )
    world = gpd.read_file(url_countries)

    url_marine_polys = (
        "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/"
        "master/geojson/ne_10m_geography_marine_polys.geojson"
    )
    marine_polys = gpd.read_file(url_marine_polys)

    return world, marine_polys