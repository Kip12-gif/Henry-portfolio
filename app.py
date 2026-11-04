import streamlit as st

st.set_page_config(
    page_title="Henry Kiplagat | GIS, Remote Sensing & Spatial Engineer",
    page_icon="🌍",
    layout="wide",
)

# ==============================================================================
# 🎨 SCIENTIFIC & PROFESSIONAL CREATIVE DESIGN SYSTEM (CSS)
# ==============================================================================
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

/* Clean Scientific Light Background with Subtle Grid */
.stApp {
    background-color: #F8FAFC;
    background-image: radial-gradient(#CBD5E1 0.8px, transparent 0.8px), 
                      radial-gradient(#CBD5E1 0.8px, #F8FAFC 0.8px);
    background-size: 36px 36px;
    background-position: 0 0, 18px 18px;
    color: #0F172A !important;
}

/* Typography Configuration */
html, body, [class*="css"], .stMarkdown, p, span, label, div {
    color: #0F172A !important;
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    font-style: normal !important;
}

/* Creative Scientific Headings */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Outfit', sans-serif !important;
    font-style: normal !important;
}

h1 {
    font-weight: 800 !important;
    letter-spacing: -1.5px;
    color: #0F172A !important;
}

/* Subheaders with Vibrant Mint/Emerald Gradient */
h2, h3 {
    font-weight: 700 !important;
    background: linear-gradient(90deg, #059669 0%, #10B981 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
    margin-bottom: 0.5rem;
}

/* Scientific Glass Cards with Elevation Hover */
div[data-testid="stBlock"] {
    background-color: #FFFFFF !important;
    border-radius: 12px !important;
    border: 1px solid #E2E8F0 !important;
    box-shadow: 0 2px 12px rgba(15, 23, 42, 0.03);
    padding: 1.8rem;
    transition: all 0.25s ease;
}
div[data-testid="stBlock"]:hover {
    border-color: #10B981 !important;
    box-shadow: 0 6px 20px rgba(16, 185, 129, 0.08);
}

/* Highly Visible Primary Buttons & Link Buttons */
div.stButton > button, div.stDownloadButton > button, a[data-testid="stLinkButton"] {
    background-color: #0F172A !important;
    color: #FFFFFF !important;
    border-radius: 6px !important;
    border: 1px solid #1E293B !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.2rem;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
    transition: all 0.2s ease;
    text-decoration: none !important;
}
div.stButton > button:hover, a[data-testid="stLinkButton"]:hover {
    background-color: #059669 !important;
    border-color: #059669 !important;
    color: #FFFFFF !important;
    transform: translateY(-1px);
}

/* Metric Display Cards */
[data-testid="stMetricValue"] {
    color: #059669 !important;
    font-weight: 800 !important;
    font-size: 2rem !important;
    font-family: 'Outfit', sans-serif !important;
}
[data-testid="stMetricLabel"] {
    color: #64748B !important;
    font-weight: 600;
}

/* Custom Styled Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: transparent;
}
.stTabs [data-baseweb="tab"] {
    background-color: #F1F5F9 !important;
    border-radius: 6px 6px 0px 0px;
    border: 1px solid #CBD5E1;
    color: #475569 !important;
    padding: 10px 20px;
    font-weight: 600;
    font-family: 'Outfit', sans-serif !important;
}
.stTabs [aria-selected="true"] {
    background-color: #0F172A !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    border: 1px solid #0F172A !important;
}

/* Tech Stack Badge Styling */
.badge {
    display: inline-block;
    padding: 4px 10px;
    margin: 2px;
    font-size: 11px;
    font-weight: 600;
    color: #059669;
    background-color: #ECFDF5;
    border: 1px solid #A7F3D0;
    border-radius: 4px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==============================================================================
# 🧭 SIDEBAR / PROFILE & NAVIGATION
# ==============================================================================
with st.sidebar:
  # Profile Image Container
  try:
    st.image("profile.jpg", use_container_width=True)
  except:
    st.image(
        "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400",
        use_container_width=True,
    )

  st.markdown("### 🌍 Henry Kiplagat")
  st.caption("GIS, Remote Sensing & Spatial Engineer")
  st.divider()

  st.markdown("**📍 Location:** Nairobi & Iten, Kenya")
  st.markdown("**🎓 Education:** B.Sc. GIS, JKUAT (2021–2025)")
  st.markdown(
      "**🛠️ Core Stack:** ArcGIS, QGIS, Python, GeoPandas, Folium, NetworkX,"
      " AutoCAD"
  )

  st.divider()
  st.markdown("### 📬 Direct Contact")
  st.markdown("📧 **Email:** kiplagathenry586@gmail.com")
  st.markdown("📞 **Phone:** +254 790 148 801")
  st.markdown(
      "🔗 **LinkedIn:**"
      " [linkedin.com/in/henry-kiplagat-aa3b26333](https://linkedin.com/in/henry-kiplagat-aa3b26333)"
  )

  st.divider()
  st.caption("© 2026 Henry Kiplagat. All rights reserved.")

# ==============================================================================
# 🏠 MAIN LANDING HEADER
# ==============================================================================
st.title("Henry Kiplagat, B.Sc. GIS 🚀")
st.markdown(
    "GIS and Remote Sensing Analyst specializing in spatial modeling, machine"
    " learning applications, telecommunication network design, and"
    " infrastructure routing."
)

# Key Metrics Row
m1, m2, m3, m4 = st.columns(4)
m1.metric("Live Web Apps", "10+ Built")
m2.metric("Domain Expertise", "RS, Survey & FTTH")
m3.metric("Modeling", "QUEFTS & Random Forest")
m4.metric("Open Source", "YouthMappers / OSM")

st.divider()

# ==============================================================================
# 📑 PORTFOLIO TABS
# ==============================================================================
tab_projects, tab_experience, tab_services, tab_skills, tab_about = st.tabs([
    "💼 Projects Hub (10 Apps)",
    "🏢 Work Experience",
    "🛠️ Consulting Services",
    "⚡ Technical Stack",
    "📖 About Me",
])

with tab_projects:
  st.markdown("## 🌟 Comprehensive Geospatial Project Hub")
  st.markdown(
      "Explore 10 production-ready mapping tools, machine learning models, and"
      " interactive web applications spanning agriculture, infrastructure, and"
      " telecommunications."
  )
  st.divider()

  # Project 1
  with st.container():
    c1, c2 = st.columns([3, 1])
    with c1:
      st.markdown(
          "### 🛢️ 1. LAPSSET Corridor — Least-Cost Pipeline Pathfinding"
      )
      st.markdown(
          "Advanced spatial network routing notebook computing optimal pipeline"
          " paths between Turkana (Lokichar) and Lamu (Mokowe) while avoiding"
          " steep escarpments and protected zones using NetworkX graph theory"
          " and DEM elevation matrices."
      )
      st.markdown(
          '<span class="badge">NetworkX</span><span'
          ' class="badge">DEM Routing</span><span'
          ' class="badge">Matplotlib</span>',
          unsafe_allow_html=True,
      )
    with c2:
      st.markdown("<br>", unsafe_allow_html=True)
      st.link_button(
          "🔗 Launch App / Repo",
          "https://github.com/yourusername/lapsset-pipeline-router",
      )
    st.divider()

  # Project 2
  with st.container():
    c1, c2 = st.columns([3, 1])
    with c1:
      st.markdown("### ☕ 2. NomadSpots — Global Workspace & Coffee Atlas")
      st.markdown(
          "Keyless remote work directory with dual-layer maps (OSM & Google"
          " Satellite), instant search, persistent user check-ins, AI"
          " workspace recommendations, and Markdown travel guide export."
      )
      st.markdown(
          '<span class="badge">Streamlit</span><span'
          ' class="badge">Folium</span><span class="badge">Pandas</span>',
          unsafe_allow_html=True,
      )
    with c2:
      st.markdown("<br>", unsafe_allow_html=True)
      st.link_button(
          "🔗 Launch App / Repo", "https://github.com/yourusername/nomad-spots"
      )
    st.divider()

  # Project 3
  with st.container():
    c1, c2 = st.columns([3, 1])
    with c1:
      st.markdown("### 🌿 3. UrbanGreen — Canopy & Carbon Tracker")
      st.markdown(
          "Neighborhood environmental registry mapping urban tree canopies,"
          " specimen health, and annual CO₂ offsets with map click-to-pin"
          " coordinate capture and Plotly forestry analytics."
      )
      st.markdown(
          '<span class="badge">GIS Mapping</span><span'
          ' class="badge">Plotly</span><span class="badge">Carbon Tracking</span>',
          unsafe_allow_html=True,
      )
    with c2:
      st.markdown("<br>", unsafe_allow_html=True)
      st.link_button(
          "🔗 Launch App / Repo", "https://github.com/yourusername/urban-green"
      )
    st.divider()

  # Project 4
  with st.container():
    c1, c2 = st.columns([3, 1])
    with c1:
      st.markdown("### 🌱 4. Fertilizer Subsidy Allocation GIS Model")
      st.markdown(
          "Final-year research project utilizing machine learning and the"
          " **QUEFTS model** integrated with soil, yield, and rainfall data"
          " to optimize smallholder farmer fertilizer distribution."
      )
      st.markdown(
          '<span class="badge">QUEFTS Model</span><span'
          ' class="badge">Machine Learning</span><span'
          ' class="badge">Python</span>',
          unsafe_allow_html=True,
      )
    with c2:
      st.markdown("<br>", unsafe_allow_html=True)
      st.link_button(
          "🔗 Launch App / Repo",
          "https://github.com/yourusername/fertilizer-subsidy-model",
      )
    st.divider()

  # Project 5
  with st.container():
    c1, c2 = st.columns([3, 1])
    with c1:
      st.markdown("### 🌽 5. Maize Yield Estimation Using WaPOR Data")
      st.markdown(
          "Remote sensing workflow processing FAO WaPOR Net Primary Production"
          " (NPP) satellite data to calculate biomass and map maize yields across"
          " Elgeyo-Marakwet County."
      )
      st.markdown(
          '<span class="badge">Remote Sensing</span><span'
          ' class="badge">WaPOR Data</span><span'
          ' class="badge">Agriculture</span>',
          unsafe_allow_html=True,
      )
    with c2:
      st.markdown("<br>", unsafe_allow_html=True)
      st.link_button(
          "🔗 Launch App / Repo",
          "https://github.com/yourusername/maize-yield-estimation",
      )
    st.divider()

  # Project 6
  with st.container():
    c1, c2 = st.columns([3, 1])
    with c1:
      st.markdown("### 🌦️ 6. Rainfall Trend Analysis Dashboard")
      st.markdown(
          "Python-automated climate analytics tool pulling multi-year NASA"
          " POWER data to visualize drought exposure and rainfall variability"
          " across agricultural regions."
      )
      st.markdown(
          '<span class="badge">NASA POWER API</span><span'
          ' class="badge">Climate Analysis</span><span'
          ' class="badge">Pandas</span>',
          unsafe_allow_html=True,
      )
    with c2:
      st.markdown("<br>", unsafe_allow_html=True)
      st.link_button(
          "🔗 Launch App / Repo",
          "https://github.com/yourusername/rainfall-trend-analysis",
      )
    st.divider()

  # Project 7
  with st.container():
    c1, c2 = st.columns([3, 1])
    with c1:
      st.markdown("### 🌐 7. SpotCheck Kenya Mobile Field App")
      st.markdown(
          "Custom mobile application project environment initialized with"
          " Flutter for crowd-sourced spot check-ins, local venue ratings, and"
          " integrated spatial mapping."
      )
      st.markdown(
          '<span class="badge">Flutter</span><span'
          ' class="badge">Mobile App</span><span'
          ' class="badge">Dart</span>',
          unsafe_allow_html=True,
      )
    with c2:
      st.markdown("<br>", unsafe_allow_html=True)
      st.link_button(
          "🔗 Launch App / Repo",
          "https://github.com/yourusername/spotcheck-kenya",
      )
    st.divider()

  # Project 8
  with st.container():
    c1, c2 = st.columns([3, 1])
    with c1:
      st.markdown("### ☕ 8. AgriCommerce Direct Coffee Trade App")
      st.markdown(
          "Agricultural e-commerce Streamlit platform linked with GitHub"
          " designed to bridge international buyers with local cooperative"
          " coffee producers for direct trade matching."
      )
      st.markdown(
          '<span class="badge">Streamlit</span><span'
          ' class="badge">Agri-Tech</span><span'
          ' class="badge">E-Commerce</span>',
          unsafe_allow_html=True,
      )
    with c2:
      st.markdown("<br>", unsafe_allow_html=True)
      st.link_button(
          "🔗 Launch App / Repo",
          "https://github.com/yourusername/agri-commerce-coffee",
      )
    st.divider()

  # Project 9
  with st.container():
    c1, c2 = st.columns([3, 1])
    with c1:
      st.markdown("### 🌍 9. Global Bucket List & Nomad Web App")
      st.markdown(
          "Interactive personal travel bucket list web application styled with"
          " a vintage notebook paper UI texture and open-source map overlays."
      )
      st.markdown(
          '<span class="badge">Web Design</span><span'
          ' class="badge">Folium</span><span class="badge">UI Styling</span>',
          unsafe_allow_html=True,
      )
    with c2:
      st.markdown("<br>", unsafe_allow_html=True)
      st.link_button(
          "🔗 Launch App / Repo",
          "https://github.com/yourusername/global-bucket-list",
      )
    st.divider()

  # Project 10
  with st.container():
    c1, c2 = st.columns([3, 1])
    with c1:
      st.markdown("### 🗺️ 10. Soil Organic Carbon & pH Mapper")
      st.markdown(
          "Raster mapping and classification of Soil Organic Carbon and soil pH"
          " datasets for Elgeyo-Marakwet County utilizing ISRIC SoilGrids"
          " spatial data."
      )
      st.markdown(
          '<span class="badge">SoilGrids</span><span'
          ' class="badge">Raster Analysis</span><span'
          ' class="badge">QGIS / Python</span>',
          unsafe_allow_html=True,
      )
    with c2:
      st.markdown("<br>", unsafe_allow_html=True)
      st.link_button(
          "🔗 Launch App / Repo",
          "https://github.com/yourusername/soil-carbon-mapper",
      )
    st.divider()

with tab_experience:
  st.markdown("## 🏢 Professional Work Experience & Internships")

  with st.container():
    st.markdown("### 🔹 Junior GIS Analyst | Anglepoint Company Ltd")
    st.caption("June 2025 – February 2026")
    st.markdown(
        """
        - Conducted spatial data clustering and advanced analysis using Python.
        - Processed and analyzed complex geospatial datasets to isolate actionable spatial patterns.
        - Developed custom scripts for automated spatial analysis workflows.
        - Produced mobile-GIS dashboards for intuitive geospatial data visualization.
        """
    )
    st.divider()

  with st.container():
    st.markdown("### 🔹 Surveyor Intern | Ministry of Lands and Physical Planning")
    st.caption("May 2024 – August 2024")
    st.markdown(
        """
        - Conducted land boundary identification and field surveys using RTK GPS, total station, and dumpy level equipment.
        - Assisted professional surveyors in preparing master plans and detailed site plans using AutoCAD.
        - Processed land mutation forms and supported cadastral data verification for accurate land parcel documentation.
        """
    )
    st.divider()

  with st.container():
    st.markdown(
        "### 🔹 YouthMappers Contributor & Volunteer | OpenStreetMap Kenya"
    )
    st.caption("September 2023 – Present | Nairobi, Kenya")
    st.markdown(
        """
        - Active contributor leveraging open-source geospatial platforms (OpenStreetMap, HOT Tasking Manager, JOSM) to map critical infrastructure.
        - Supported humanitarian response efforts and generated high-quality open spatial data across Kenya.
        """
    )

with tab_services:
  st.markdown("## 🛠️ Professional Consulting Services")
  st.markdown(
      "Specialized consultancy services built on field experience, advanced"
      " remote sensing, machine learning modeling, and telecommunication network"
      " engineering."
  )

  c1, c2 = st.columns(2)
  with c1:
    with st.container():
      st.markdown("### 🛰️ Remote Sensing, Photogrammetry & GIS Analysis")
      st.markdown(
          "High-precision satellite image classification, UAV/drone imagery"
          " photogrammetry, change detection, spatial modeling, and automated GIS"
          " workflow scripting."
      )
    with st.container():
      st.markdown("### 📐 Land, Topographic & Engineering Surveying")
      st.markdown(
          "Cadastral boundary surveys, topographic mapping, construction"
          " layout, and site data collection using RTK GPS, Total Stations,"
          " and Dumpy Levels."
      )
  with c2:
    with st.container():
      st.markdown("### 🤖 Machine Learning & Agricultural Modeling")
      st.markdown(
          "Predictive modeling using Random Forest algorithms, crop yield"
          " estimations, and soil-crop simulation through the **QUEFTS model**."
      )
    with st.container():
      st.markdown("### 🔌 Fiber To The Home (FTTH) Network Design")
      st.markdown(
          "End-to-end telecommunication network planning, GIS-based FTTx route"
          " design, splitters placement, and bill of materials (BoM) spatial"
          " mapping."
      )

with tab_skills:
  st.markdown("## ⚡ Technical Stack & Core Competencies")

  s1, s2 = st.columns(2)
  with s1:
    st.markdown("### 💻 Software & Programming")
    st.markdown(
        """
        - **GIS & RS Software:** ArcGIS, QGIS, Global Mapper
        - **Programming:** Python (GeoPandas, Pandas, NumPy, NetworkX, Scikit-Learn)
        - **Surveying & Engineering:** AutoCAD, RTK GPS, Total Station, Dumpy Level
        - **Web & Telecom:** Web GIS, GeoServer, Folium, Streamlit, FTTH Design Tools
        """
    )
  with s2:
    st.markdown("### 🎯 Core Competencies")
    st.markdown(
        """
        - Remote Sensing & Photogrammetry
        - Machine Learning (Random Forest, QUEFTS Model)
        - FTTH Network Planning & Design
        - Topographic, Land & Engineering Surveying
        - Spatial Data Analysis & Geostatistics
        - Cartography & Map Design
        """
    )

with tab_about:
  st.markdown("## 📖 About Me")
  st.markdown(
      "I am a detail-oriented GIS and Remote Sensing analyst holding a Bachelor"
      " of Science degree in GIS from Jomo Kenyatta University of Agriculture"
      " and Technology (JKUAT). Based in Kenya, I combine technical"
      " proficiency in machine learning, remote sensing, and Python scripting"
      " with field experience in land surveying, photogrammetry, and"
      " telecommunication FTTH network design."
  )
  st.markdown(
      "Committed to deploying spatial intelligence to solve real-world"
      " challenges in agriculture, climate action, and infrastructure, I have"
      " built decision-support models using the QUEFTS framework, designed"
      " multi-platform web applications, and actively contribute open spatial"
      " data through YouthMappers and OpenStreetMap."
  )
