import dash  # (version 1.12.0) pip install dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px  # (version 4.7.0)
from dash import html


from walkscore import WalkScoreAPI\


API_KEY = '62c5d8bc355352b5fe686514763ed6cc'

# ------------------------------------------------------------------------------
# Start app add Bootstraps Theme

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])
server = app.server

# ------------------------------------------------------------------------------
# Start app add Bootstraps Theme

#app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])
#server = app.server

# ------------------------------------------------------------------------------
# Import and clean data (importing  csv into pandas)



app.layout = html.Div([

])


score = WalkScoreAPI(api_key=API_KEY)


result = score.get_score(longitude=-80.063229,
                         latitude=40.381855,
                         address='804 Linda Ln, Pittsburgh, PA 15243, USA',
                         return_transit_score="False",
                         )


r=result.to_dict()

df2 = pd.DataFrame.from_dict(r)


df3 =df2.drop(columns =['logo_url', 'more_info_icon','more_info_link','help_link','property_page_link','snapped_coordinates','transit','status','walk'], axis=1)
df3

df4=df3.transpose()
df4

df5 = df4.fillna(0)
df5['longitude'] = df5['longitude'].shift(-1)
df5['latitude'] = df5['latitude'].shift(-1)
df5['address'] = df5['address'].shift(-1)
df6=df5.drop('original_coordinates', axis ='rows')
walk_ad = result.to_dict()



fig = px.scatter_mapbox(df5, lat='latitude', lon='longitude', hover_name="address", hover_data=["score", "description"],
                            color_discrete_sequence=["fuchsia"], zoom=15, height=500,
                              )
                            #color='Type of bear', zoom=3=10, height=500)
fig.update_layout(mapbox_style="open-street-map",title='Ebike Score: Hover over the fushia point to see the bike score and description of the property.')
fig.update_layout(margin={"r": 100, "t": 100, "l": 10, "b": 10})
  

fig.show()




if __name__ == '__app__':
    app.run_server(debug=True, HOST="0.0.0.0", port=8080)


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
