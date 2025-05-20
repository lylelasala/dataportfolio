import streamlit as st

# Apple Music embed code (cleaned up)
apple_music_embed = """
<iframe allow="autoplay *; encrypted-media *; fullscreen *; clipboard-write" frameborder="0"
height="150" style="width:100%;max-width:660px;overflow:hidden;border-radius:10px;"
sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-top-navigation-by-user-activation"
src="https://embed.music.apple.com/us/song/good-morning-baby/1445666384"></iframe>
"""

# Streamlit app layout
st.title("┬─┬ ☕︎ノ( º , ºノ) Internet Café")
st.subheader("Prototype")

# Display "Song of the Day"
st.write("🎵 **Song of the Day:** Good Morning Baby - Dan Wilson & Bic Runga")

# Embed Apple Music player
st.components.v1.html(apple_music_embed, height=175)

# Portfolio projects
st.header("Projects")
projects = {
    "American Sign Language Finger Spelling Recognition": "https://www.strongasl.com/learn/home",
    "Asian American Philippine Basketball Association Statbook": "https://www.facebook.com/photo.php?fbid=975154716181166&set=a.105158656514114&type=3",
    "Photography Projects": "https://vsco.co/spaces/680333f275b118ae4c57213f"
}

for project, link in projects.items():
    st.write(f"[{project}]({link})")

# Footer (added working link)
st.write("🔗 [Visit my full portfolio](https://www.datascienceportfol.io/lyleblueberry)")
