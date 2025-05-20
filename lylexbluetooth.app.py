import streamlit as st

# Apple Music embed code (cleaned up)
apple_music_embed = """
<iframe allow="autoplay *; encrypted-media *; fullscreen *; clipboard-write" frameborder="0"
height="150" style="width:100%;max-width:660px;overflow:hidden;border-radius:10px;"
sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-top-navigation-by-user-activation"
src="https://embed.music.apple.com/us/song/good-morning-baby/1445666384"></iframe>
"""

# Streamlit app layout
st.title("┬─┬ ☕︎ノ( º , ºノ) internet café")
st.subheader("prototype")

# Display "Song of the Day"
st.write("🎵 **Song of the Day:** Good Morning Baby - Dan Wilson & Bic Runga")

# Embed Apple Music player
st.components.v1.html(apple_music_embed, height=175)

# Portfolio projects
st.header("projects")
projects = {
    "american sign language finger spelling recognition": "https://www.strongasl.com/learn/home",
    "asian american philippine basketball association statbook": "https://www.facebook.com/photo.php?fbid=975154716181166&set=a.105158656514114&type=3",
    "photography projects": "http://vsco.co/bluetoothbrownheartdotmp4?share=MTc0NTAzOTc3Mg%3D%3D"
}

for project, link in projects.items():
    st.write(f"[{project}]({link})")

# Footer (added working link)
st.write("🔗 [visit my full portfolio]")
