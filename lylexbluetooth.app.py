import streamlit as st

# SoundCloud Embed Code with Interactive Player
soundcloud_embed = """
<iframe width="100%" height="155" scrolling="no" frameborder="no" allow="autoplay"
src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1530937807&color=%238f5a4b&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>
"""

# Streamlit App Layout
st.title("┬─┬ ☕︎ノ( º , ºノ) internet café")
st.subheader("*prototype")

# Display "Song of the Day"
st.write("🔊 **** Kendrick Lamar - The Hillbillies (2000s remix)")

# Embed SoundCloud Player
st.components.v1.html(soundcloud_embed, height=150)

# Portfolio Projects
st.header("proj.")
projects = {"soundtrap": "https://www.soundtrap.com/home/creator/projects/folders/63644883"
}

for project, link in projects.items():
    st.write(f"[{project}]({link})")

# Footer (added working link)
st.write("🔗 [Visit my full portfolio](https://bluetoothbrownheartdotmp4.streamlit.app/)")

