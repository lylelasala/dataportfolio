import streamlit as st

# SoundCloud Embed Code with Duke Blue Color
soundcloud_embed = """
<iframe width="100%" height="155" scrolling="no" frameborder="no" allow="autoplay"
src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1530937807&color=%2300009C&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>
<div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;">
<a href="https://soundcloud.com/savingconnie" title="Saving Connie Skywalker" target="_blank" style="color: #cccccc; text-decoration: none;">Saving Connie Skywalker</a> · 
<a href="https://soundcloud.com/savingconnie/kendrick-lamar-the-hillbillies-2000s-remix" title="Kendrick Lamar - The Hillbillies (2000s remix)" target="_blank" style="color: #cccccc; text-decoration: none;">Kendrick Lamar - The Hillbillies (2000s remix)</a>
</div>
"""

# Streamlit App Layout
st.title("┬─┬ ☕︎ノ( º , ºノ) internet café")
st.subheader("*prototype")

# Display "Song of the Day"
st.write("🔊 **** kendrick lamar - the hillbillies (2000s remix)")

# Embed SoundCloud Player with Duke Blue Color
st.components.v1.html(soundcloud_embed, height=155)

# Portfolio Projects
st.header("proj.")
projects = {
    "soundtrap": "https://www.soundtrap.com/home/creator/projects/folders/63644883",
    "yt": "https://youtube.com/playlist?list=PL26G5xKQCDOoiWrix94v6coGvchbwQHqI&si=3m16g4CKtS21rOY6"
}

for project, link in projects.items():
    st.write(f"[{project}]({link})")

# Footer (added working link)
st.write("🔗 [Visit my full portfolio](https://bluetoothbrownheartdotmp4.streamlit.app/)")
