import streamlit as st

st.set_page_config(
    page_title="Henry Kiplagat | GIS & Remote Sensing Analyst",
    page_icon="🌍",
    layout="wide",
)

# ==============================================================================
# 🎨 PROFESSIONAL SLATE & BOTANICAL DESIGN SYSTEM (CSS)
# ==============================================================================
custom_css = """
<style>
/* Clean Professional Light Background with Subtle Grid */
.stApp {
    background-color: #F8FAFC;
    background-image: radial-gradient(#E2E8F0 0.75px, transparent 0.75px), 
                      radial-gradient(#E2E8F0 0.75px, #F8FAFC 0.75px);
    background-size: 32px 32px;
    background-position: 0 0, 16px 16px;
    color: #0F172A !important;
}

/* High-Contrast Typography */
html, body, [class*="css"], .stMarkdown, p, span, label, h1, h2, h3, h4, h5, h6 {
    color: #0F172A !important;
    font-family: 'Inter', -apple-system, sans-serif;
}

/* Header Styling */
h1 {
    font-weight: 800;
    letter-spacing: -1.5px;
    color: #0F172A !important;
}
h2, h3 {
    color: #1E293B !important;
    font-weight: 700;
}

/* Professional White Glass Cards */
div[data-testid="stBlock"] {
    background-color: #FFFFFF !important;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04);
    padding: 1.6rem;
}

/* Primary Action Buttons */
div.stButton > button, div.stDownloadButton > button {
    background-color: #0F172A !important;
    color: #FFFFFF !important;
    border-radius: 8px !important;
    border: none !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
    transition: all 0.2s ease;
}
div.stButton > button:hover {
    background-color: #334155 !important;
    transform: translateY(-1px);
}

/* Metric Display Cards */
[data-testid="stMetricValue"] {
    color: #0F172A !important;
    font-weight: 800 !important;
    font-size: 2.2rem !important;
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
    border-radius: 8px 8px 0px 0px;
    border: 1px solid #CBD5E1;
    color: #475569 !important;
    padding: 10px 20px;
    font-weight: 600;
}
.stTabs [aria-selected="true"] {
    background-color: #0F172A !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    border: 1px solid #0F172A;
}

/* Badge Styling */
.badge {
    display: inline-block;
    padding: 4px 10px;
    margin: 2px;
    font-size: 12px;
    font-weight: 600;
    color: #0F172A;
    background-color: #E2E8F0;
    border-radius: 6px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==============================================================================
# 🧭 SIDEBAR / NAVIGATION & PROFILE SUMMARY
# ==============================================================================
with st.sidebar:
  st.markdown("### 🌍 Henry Kiplagat")
  st.caption("GIS & Remote Sensing Analyst")
  st.divider()

  st.markdown("**📍 Location:** Nairobi & Iten, Kenya[cite: 1]")
  st.markdown("**🎓 Education:** B.Sc. GIS, JKUAT (2021–2025)[cite: 1, 2]")
  st.markdown(
      "**🛠️ Core Stack:** ArcGIS, QGIS, Python, GeoPandas, Folium, NetworkX,"
      " AutoCAD"
  )

  st.divider()
  st.markdown("### 📬 Direct Contact")
  st.markdown("📧 **Email:** kiplagathenry586@gmail.com[cite: 1]")
  st.markdown("📞 **Phone:** +254 790 148 801[cite: 1]")
  st.markdown(
      "🔗 **LinkedIn:**"
      " [linkedin.com/in/henry-kiplagat-aa3b26333](https://linkedin.com/in/henry-kiplagat-aa3b26333)"
      "[cite: 1]"
  )

  st.divider()
  st.caption("© 2026 Henry Kiplagat. All rights reserved.")

# ==============================================================================
# 🏠 MAIN LANDING HEADER
# ==============================================================================
st.title("Hi, I'm Henry Kiplagat 🚀")
st.markdown(
    "### *GIS & Remote Sensing Analyst specializing in spatial analysis,"
    " infrastructure routing, satellite data interpretation, and agricultural"
    " decision-support systems.*"
)

# Key Metrics Row
m1, m2, m3, m4 = st.columns(4)
m1.metric("Featured Projects", "6 Core Works")
m2.metric("Mapping Engines", "ArcGIS / QGIS / Folium")
m3.metric("Key Domain", "Agri-Tech & Infrastructure")
m4.metric("Open Source", "YouthMappers / OSM")

st.divider()

# ==============================================================================
# 📑 PORTFOLIO TABS
# ==============================================================================
tab_projects, tab_experience, tab_services, tab_skills, tab_about = st.tabs([
    "💼 Projects & Portfolio",
    "🏢 Work Experience",
    "🛠️ Consulting Services",
    "⚡ Technical Stack",
    "📖 About Me",
])

with tab_projects:
  st.markdown("## 🌟 Comprehensive Geospatial Project Portfolio")
  st.markdown(
      "Explore production-ready mapping tools, spatial models, and interactive"
      " web applications bridging infrastructure, climate data, and agriculture."
  )

  # Project 1: LAPSSET Pipeline Router
  with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
      st.markdown(
          "### 🛢️ LAPSSET Corridor — Least-Cost Pipeline Pathfinding"
      )
      st.markdown(
          "An advanced spatial network routing notebook that calculates the"
          " safest and most efficient pipeline corridor between the Lokichar"
          " Oil Fields (Turkana) and Mokowe Refinery (Lamu, Kenya). Integrates"
          " graph theory (`NetworkX`), terrain elevation matrices, and"
          " automated elevation profiling to navigate around escarpments and"
          " protected zones."
      )
      st.markdown(
          '<span class="badge">NetworkX Graph Theory</span><span'
          ' class="badge">DEM Routing</span><span'
          ' class="badge">Matplotlib</span>',
          unsafe_allow_html=True,
      )
    with col2:
      st.markdown("<br>", unsafe_allow_html=True)
      if st.button("View Routing Details", key="proj_lapsset"):
        st.info("Advanced least-cost path analysis and elevation profiling.")
    st.divider()

  # Project 2: NomadSpots Workspace Atlas
  with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
      st.markdown("### ☕ NomadSpots — Global Workspace Atlas")
      st.markdown(
          "A keyless, interactive workspace directory and global map tailored"
          " for remote workers. Features dual-layer maps (OpenStreetMap & Google"
          " Satellite), instant keyword filtering, community check-ins with"
          " session state persistence, an AI workspace recommendation engine,"
          " and exportable Markdown travel guides."
      )
      st.markdown(
          '<span class="badge">Streamlit</span><span'
          ' class="badge">Folium</span><span'
          ' class="badge">Pandas</span><span class="badge">Zero-API</span>',
          unsafe_allow_html=True,
      )
    with col2:
      st.markdown("<br>", unsafe_allow_html=True)
      if st.button("View NomadSpots", key="proj_nomad"):
        st.info("Interactive geo-web directory application.")
    st.divider()

  # Project 3: UrbanGreen Canopy Tracker
  with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
      st.markdown("### 🌿 UrbanGreen — Canopy & Carbon Tracker")
      st.markdown(
          "A neighborhood environmental geospatial registry that maps urban"
          " tree canopies, tracks specimen health conditions, and calculates"
          " estimated annual CO₂ offsets. Includes map click-to-pin coordinate"
          " capture and interactive Plotly forestry analytics."
      )
      st.markdown(
          '<span class="badge">Geospatial GIS</span><span'
          ' class="badge">Plotly Analytics</span><span'
          ' class="badge">Environmental Science</span>',
          unsafe_allow_html=True,
      )
    with col2:
      st.markdown("<br>", unsafe_allow_html=True)
      if st.button("View UrbanGreen", key="proj_urban"):
        st.info("Environmental carbon offset and tree registry app.")
    st.divider()

  # Project 4: Fertilizer Subsidy Model
  with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
      st.markdown("### 🌱 Fertilizer Subsidy Allocation GIS Model")
      st.markdown(
          "A spatial decision-support model integrating yield, soil, and"
          " rainfall data to estimate precise fertilizer requirements using"
          " the **QUEFTS model** and machine learning. Built as a final-year"
          " research project to optimize fertilizer distribution and target"
          " smallholder farmers effectively."
      )
      st.markdown(
          '<span class="badge">QUEFTS Model</span><span'
          ' class="badge">Machine Learning</span><span'
          ' class="badge">Python</span><span class="badge">Spatial'
          ' Modeling</span>',
          unsafe_allow_html=True,
      )
    with col2:
      st.markdown("<br>", unsafe_allow_html=True)
      if st.button("View Research Details", key="proj_sub"):
        st.info("Final-year research application focused on agricultural optimization.")
    st.divider()

  # Project 5: Maize Yield Estimation
  with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
      st.markdown("### 🌽 Maize Yield Estimation Using WaPOR Data")
      st.markdown(
          "Processed satellite Net Primary Production (NPP) data from FAO WaPOR"
          " to evaluate biomass accumulation and generate high-resolution"
          " maize yield maps for Elgeyo-Marakwet County, supporting regional"
          " food security monitoring."
      )
      st.markdown(
          '<span class="badge">Remote Sensing</span><span'
          ' class="badge">WaPOR Satellite Data</span><span'
          ' class="badge">Agricultural GIS</span>',
          unsafe_allow_html=True,
      )
    with col2:
      st.markdown("<br>", unsafe_allow_html=True)
      if st.button("View Maize Details", key="proj_maize"):
        st.info("Remote sensing workflow evaluating regional biomass and yield.")
    st.divider()

  # Project 6: Rainfall Trend Analysis
  with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
      st.markdown("### 🌦️ Rainfall Trend Analysis in Kenya")
      st.markdown(
          "Analyzed NASA POWER multi-year climate data using Python scripts to"
          " visualize spatial rainfall variability, climate trends, and drought"
          " exposure patterns across agricultural zones in Kenya."
      )
      st.markdown(
          '<span class="badge">Climate Analysis</span><span'
          ' class="badge">NASA POWER API</span><span'
          ' class="badge">Python</span>',
          unsafe_allow_html=True,
      )
    with col2:
      st.markdown("<br>", unsafe_allow_html=True)
      if st.button("View Climate Details", key="proj_rain"):
        st.info("Climatological trend analysis using automated Python scripting.")
    st.divider()

with tab_experience:
  st.markdown("## 🏢 Professional Work Experience & Internships")

  with st.container():
    st.markdown("### 🔹 Junior GIS Analyst | Anglepoint Company Ltd")
    st.caption("*June 2025 – February 2026*")
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
    st.caption("*May 2024 – August 2024*")
    st.markdown(
        """
        - Conducted land boundary identification and rigorous field surveys using RTK GPS, total station, and dumpy level equipment.
        - Assisted professional surveyors in preparing master plans and detailed site plans using AutoCAD.
        - Processed land mutation forms and supported cadastral data verification for accurate land parcel documentation.
        """
    )
    st.divider()

  with st.container():
    st.markdown(
        "### 🔹 YouthMappers Contributor & Volunteer | OpenStreetMap Kenya"
    )
    st.caption("*September 2023 – Present | Nairobi, Kenya*[cite: 2]")
    st.markdown(
        """
        - Active contributor leveraging open-source geospatial platforms (OpenStreetMap, HOT Tasking Manager, JOSM) to map critical infrastructure[cite: 2].
        - Supported humanitarian response efforts and generated high-quality open spatial data across Kenya[cite: 2].
        """
    )

with tab_services:
  st.markdown("## 🛠️ Professional Consulting Services")
  st.markdown(
      "Delivering end-to-end geospatial solutions for infrastructure,"
      " agriculture, land management, and spatial web applications."
  )

  c1, c2, c3 = st.columns(3)
  with c1:
    with st.container():
      st.markdown("### 🛢️ Infrastructure & Routing")
      st.markdown(
          "Least-cost path analysis, corridor planning, terrain modeling, and"
          " spatial network routing for major infrastructure projects."
      )
  with c2:
    with st.container():
      st.markdown("### 🌾 Agricultural & Environmental GIS")
      st.markdown(
          "Crop yield estimation, soil health mapping, precision fertilizer"
          " subsidy allocation models, and carbon offset tracking."
      )
  with c3:
    with st.container():
      st.markdown("### 🌐 Geo-Web Development")
      st.markdown(
          "Interactive web maps, mobile-compliant dashboards, and keyless"
          " spatial applications built with Streamlit, Folium, and Python."
      )

with tab_skills:
  st.markdown("## ⚡ Technical Stack & Core Competencies")

  s1, s2 = st.columns(2)
  with s1:
    st.markdown("### 💻 Software & Programming")
    st.markdown(
        """
        - **GIS Software:** ArcGIS, QGIS, Global Mapper[cite: 1, 2]
        - **Programming & Scripting:** Python (GeoPandas, Pandas, NumPy, NetworkX)[cite: 1]
        - **Surveying Tools:** RTK GPS, Total Station, Dumpy Level, AutoCAD[cite: 1, 2]
        - **Web & Cloud GIS:** Web GIS, GeoServer, Folium, Streamlit[cite: 2]
        """
    )
  with s2:
    st.markdown("### 🎯 Core Competencies")
    st.markdown(
        """
        - Cartography & Map Design[cite: 2]
        - Remote Sensing & Satellite Image Interpretation[cite: 1, 2]
        - Spatial Data Analysis & Geostatistical Modeling[cite: 1, 2]
        - GPS & Field Data Collection[cite: 2]
        - UAV / LiDAR Data Processing[cite: 2]
        - Cadastral & Engineering Surveying[cite: 2]
        """
    )

with tab_about:
  st.markdown("## 📖 About Me")
  st.markdown(
      "I am a detail-oriented GIS and Remote Sensing analyst holding a Bachelor"
      " of Science degree in GIS from Jomo Kenyatta University of Agriculture"
      " and Technology (JKUAT)[cite: 1, 2]. Based in Kenya, I combine"
      " technical expertise in spatial analysis, remote sensing, and Python"
      " scripting with hands-on experience in cadastral surveying, land"
      " administration[cite: 1, 2], and geo-web application development."
  )
  st.markdown(
      "Passionate about applying geospatial technology to solve real-world"
      " challenges in agriculture, climate action, and infrastructure [cite:"
      " 1], I have engineered data-driven models like fertilizer subsidy allocation"
      " algorithms using the QUEFTS framework, least-cost routing for"
      " corridors, and interactive web maps, while actively contributing open"
      " spatial data through YouthMappers and OpenStreetMap[cite: 2]."
  )