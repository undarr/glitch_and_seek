import streamlit as st
import streamlit.components.v1 as components
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import keyboard
import threading
import sys
from frontend import fendfile
from datetime import datetime
st.set_page_config(layout="wide")
'''
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Optional: run headless
options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=options)
driver.get("https://codeshare.io/ueue")
code_mirror_editor_div = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.CodeMirror")))
initial_code = driver.execute_script("return arguments[0].CodeMirror.getValue();", code_mirror_editor_div)
'''
initial_code = "test"
props = {'initial_state': initial_code}
value = fendfile(key='toggle_buttons', **props)
st.header('Streamlit')
st.write('Received from component: ', value)

