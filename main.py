import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go

# load the data
vdf = pd.read_excel("table04a.xlsx")
usa_map = gpd.read_file("cb_2018_us_state_20m/cb_2018_us_state_20m.shp")

# clean the data
vdf.loc[:, "state"] = vdf.state.str.upper()
usa_map.loc[:, "NAME"] = usa_map.NAME.str.upper()
vdf.rename(columns={"state": "NAME"}, inplace=True)

# merge with location data
merged_df = usa_map.merge(vdf, how="outer", on="NAME")

# plot
fig = go.Figure(data=go.Choropleth(
    locations=merged_df.STUSPS, # Spatial coordinates
    z = merged_df.percent_voted_citizen, # Data to be color-coded
    locationmode = "USA-states", # set of locations match entries in `locations`
    colorscale=[(0, "white"), (1, "rgba(255, 77, 77, 0.75)")],
    marker_line_color="white",
    colorbar_title="VEP Turnout"
))

fig.update_layout(
    title_text="2020 US Presidential Election VEP Turnout by State",
    geo_scope="usa"
)

fig.show()
# fig.write_image("vep_by_state.png")
