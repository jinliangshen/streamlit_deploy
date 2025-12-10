import streamlit as st

# 配置页面（保持不变）
st.set_page_config(
    page_title="你的应用标题",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={'Get Help': None, 'Report a bug': None, 'About': None}
)

# 增强 CSS：隐藏右下角图标、footer、toolbar 等
st.markdown("""
<style>
    /* 隐藏 footer 和 viewer badge */
    footer { visibility: hidden !important; }
    .viewerBadge_container__1QS0b { display: none !important; }
    div[data-testid="stToolbar"] { visibility: hidden !important; height: 0% !important; position: fixed !important; }
    div[data-testid="stDecoration"] { visibility: hidden !important; height: 0% !important; position: fixed !important; }
    div[data-testid="stStatusWidget"] { visibility: hidden !important; height: 0% !important; position: fixed !important; }
    
    /* 隐藏 header、菜单和加载条 */
    header { visibility: hidden !important; }
    #MainMenu { visibility: hidden !important; height: 0% !important; }
    .st-emotion-cache-1r4w99b { display: none !important; }
    .stProgress > div > div > div > div { background-color: transparent !important; }
    
    /* 额外：隐藏侧边栏和 iframe 全屏 */
    section[data-testid="stSidebar"] { display: none !important; }
    .stAppViewContainer { padding: 0 !important; margin: 0 !important; }
</style>
""", unsafe_allow_html=True)

st.title("Hello, Streamlit!")