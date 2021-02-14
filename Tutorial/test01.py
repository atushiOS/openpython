import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk

st.title('Streamlit 超入門')
st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70] ,
    columns = ['lat', 'lon']
)

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/streets-v11',
    initial_view_state=pdk.ViewState(
        latitude=35.69,
        longitude=139.70,
        zoom=11,
        pitch=60,
    ),
    # layers=[
    #     pdk.Layer(
    #         'HexagonLayer',
    #         data=df,
    #         get_position='[lon, lat]',
    #         radius=200,
    #         elevation_scale=4,
    #         elevation_range=[0, 1000],
    #         pickable=True,
    #         extruded=True,
    #     ),
    #     pdk.Layer(
    #         'ScatterplotLayer',
    #         data=df,
    #         get_position='[lon, lat]',
    #         get_color='[200, 30, 0, 160]',
    #         get_radius=200,
    #     ),
    # ],
))

# st.map(df)

# st.line_chart(df)

# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """