import streamlit as st
from lib.utils import create_connection

#pages/db/bi/src/lib/utils.py
# make sure the db exists irrespective of where user comes from
create_connection('core.db')


# just paste most of your medium arcticle here 
st.markdown("""# Intro

Data Analysis doesn't need to be hard. You can keep things very simple and still
achieve all of the insights you need while moving fast. 

This app serves as a simple demo of a lightweight approach to this. Add in 
DBT and Dagster and you really do have all you need. pip installable business 
analysis.

This is a one database analytics tool, whatever CSV you upload will end up in
the same SQLite file behind the scenes.

## Features 
- [ ] Connect to Snowflake.
- [ ] Way to delete queries.
- [ ] Integrate DBT / smoothly work with it 
- [x] Save and load queries.
- [ ] SSO with facebook / google / azure login
- [x] Remove the select y axis and x axis in favour of using 1st for X etc.
- [x] Create API endpoint to return query results
- [ ] Open-source a way to create forms with streamlit
- [ ] Apply the same process / system to your QDrant UI
- [ ] Submit to Analytics Vidhya
- [ ] Should have table name as query to follow single entity convention.
- [ ] Add method to save chart config (e.g. bar vs line vs scatter)
- [ ] Do the same for a Vector Database with json queries!

A self-serve API. Written up in more depth here https://medium.com/p/cd6a9ba8a48f

BI tools like Tableau, Metabase, Mode, Looker, lightdash (and more!) offer 
a way to grab hold of data in different ways and illustrate its present impact.

```
uvicorn api:app --reload
```

""")