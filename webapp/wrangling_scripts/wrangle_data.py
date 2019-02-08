import pandas as pd
import plotly.graph_objs as go

def cleandata(data, keep_columns=["Country Name", "1990", "2015"], 
              value_variables=["1990", "2015"]):
    """Clean world bank data for a visualizaiton dashboard

    Keeps data range of dates in keep_columns variable and data for the top 10 
    economies
    Reorients the columns into a year, country and value

    Args:
        dataset (str): name of the csv data file
        keep_columns (list): columns to retain in dataset
        value_variables (list): value variables for melt

    Returns:
        pandas dataframe

    """
    df = pd.read_csv(data, skiprows=4) # Not sure why skiprows is used

    # Keep only the columns of interest (year and country name)
    df = df[keep_columns]

    top10country = ['United States', 'China', 'Japan', 'Germany', 
                    'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 
                    'Canada']
    df = df[df["Country Name"].isin(top10country)]

    # Melt columns and convert year to date time
    df_melt = df.melt(id_vars="Country Name", value_vars=value_variables)
    df_melt.columns = ["country", "year", "variable"]
    df_melt["year"] = df_melt["year"].astype("datetime64[ns]").dt.year

    return df_melt

def return_figures():
    """Creates five plotly vizualizations

    Args:
        None
    Returns:
        list (dict): list containing plotly visualizations
    """
    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    graph_one = []
    df = cleandata("data/API_AG.LND.ARBL.HA.PC_DS2_en_csv_v2.csv")
    df.columns = ["country", "year", "arable_land_perperson_ha"]
    df.sort_values("arable_land_perperson_ha", ascending=False, inplace=True)
    countrylist = df.country.unique().tolist()

    for country in countrylist:
        # For plotly visualizations, values must be in a list
        x_val = df[df["country"] == country].year.tolist()
        y_val = df[df["country"] == country].arable_land_perperson_ha.tolist()
        # Create a different go Scatter object for each country
        graph_one.append(
            go.Scatter(x=x_val, y=y_val, mode="lines", name=country)
        )
    
    layout_one = {
        "title": "Change in Hectares of Arable Land <br> per Person 1990 to 2015",
        "xaxis": {
            "title": "Year",
            "autotick": False,
            "tick0": 1990,
            "dtick": 25
        },
        "yaxis": {
            "title": "Hectares"
        },
    }

    # Second chart plots ararble land for 2015 as a bar chart
    graph_two = []
    # Able to reuse data from first plot
    df = df[df["year"] == 2015]

    graph_two.append(
        go.Bar(x=df.country.tolist(), y=df.arable_land_perperson_ha.tolist())
    )

    layout_two = {
        "title": "Hectares Arable Land per Person in 2015",
        "xaxis": {"title": "Country"},
        "yaxis": {"title": "Arable Land per Person (ha)"},
    }

    # Third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    df = cleandata("data/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_9948275.csv")
    df.columns = ["country", "year", "percentrural"]
    df.sort_values("percentrural", ascending=False, inplace=True)
    for country in countrylist:
        x_val = df[df["country"] == country].year.tolist()
        y_val = df[df["country"] == country].percentrural.tolist()
        graph_three.append(
            go.Scatter(x=x_val, y=y_val, mode="lines", name=country)
        )
    
    layout_three = {
        "title": "Percentage of Population that is Rural <br> from 1990 to 2015",
        "xaxis": {
            "title": "Country",
            "autoticks": False,
            "tick0": 1990,
            "dtick": 25},
        "yaxis": {
            "title": "Percentage of Population"
        },
    }

    # Fourth chart shows rural population vs arable land
    graph_four = []

    valuevariables = [str(x) for x in range(1995, 2016)]
    keepcolumns = [str(x) for x in range(1995, 2016)]
    keepcolumns.insert(0, "Country Name")

    df_one = cleandata("data/API_SP.RUR.TOTL_DS2_en_csv_v2_9914824.csv",
                       keepcolumns, valuevariables)
    df_two = cleandata("data/API_AG.LND.FRST.K2_DS2_en_csv_v2_9910393.csv",
                       keepcolumns, valuevariables)
    
    cols = ["country", "year", "variable"]
    df_one.columns = cols
    df_two.columns = cols

    df = df_one.merge(df_two, on=["country", "year"])

    for country in countrylist:
        x_val = df[df["country"] == country].variable_x.tolist()
        y_val = df[df["country"] == country].variable_y.tolist()
        year = df[df["country"] == country].year.tolist()
        country_label = df[df["country"] == country].country.tolist()

        text = [] # I think this creates text for the markers in the plot
        for country, year in zip(country_label, year):
            text.append(str(country) + " " + str(year))

        graph_four.append(
            go.Scatter(x=x_val, y=y_val, mode="markers", text=text, 
                       name=country, textposition="top center")
        )
    
    layout_four = {
        "title": "Rural Population versus <br> Forested Area (Square Km) 1990-2015",
        "xaxis": {"title": "Rural Population"},
        "yaxis": {"title": "Forest Area (sq. km)"},
    }

    # Fifth chart shows the rural population in 2015
    graph_five = []

    df = cleandata("data/API_SP.RUR.TOTL_DS2_en_csv_v2_9914824.csv")
    df.columns = ["country", "year", "rural_population"]
    df.sort_values("rural_population", ascending=False, inplace=True)

    graph_five.append(
        go.Bar(x=df.country.tolist(), y=df.rural_population.tolist())
    )

    layout_five = {
        "title": "Rural Population in 2015",
        "xaxis": {"title": "Country"},
        "yaxis": {"title": "Population"},
    }

    # Append all charts to figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five, layout=layout_five))

    return figures