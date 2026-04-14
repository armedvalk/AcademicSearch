from dearpygui import dearpygui as dpg
import os
import requests
import pyautogui as pag
import pyperclip
ALEX_API_KEY = os.getenv("SEARCH_API_KEY")
def searchPaper(search_term):
results=requests.get("https://api.openalex.org/works?search.semantic=search_term&api_key=ALEX_API_KEY")
returnWindoow=pag.alert(text=results,title="Academic Database Scrape Results",buttons="Ok","Copy")
if returnWindoow=="Copy":
  pyperclip.copy(results)
def contextDPG(): 
  dpg.create_context()
  dpg.create_viewport(title='Academia Search', width=600, height=300)
  

  with dpg.window(label="Example Window"):
      dpg.add_text("Hello, world")
      dpg.add_button(label="Save")
      search_term=dpg.add_input_text(label="Search Query", default_value="AI and Mental Health")


  dpg.setup_dearpygui() 
  dpg.show_viewport()
  dpg.start_dearpygui()
  dpg.destroy_context()
