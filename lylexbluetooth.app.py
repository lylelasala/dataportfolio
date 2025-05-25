import streamlit as st

# Clickable Profile Picture Linked to Instagram
st.markdown(
    """
    <a href="https://www.instagram.com/p/CHQ1XxCH6eZ/" target="_blank">
        <img src="profile pic.jpg" alt="📸 haha" width="250" style="border-radius:10px;">
    </a>
    """,
    unsafe_allow_html=True
)

# SoundCloud Embed Code with Blue Color
soundcloud_embed = """
<iframe width="100%" height="155" scrolling="no" frameborder="no" allow="autoplay"
src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1747281948&color=%2300009C&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>
<div style="font-size: 10px; color: #cccccc; line-break: anywhere; word-break: normal; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; font-family: Interstate, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Garuda, Verdana, Tahoma, sans-serif; font-weight: 100;">
<a href="https://soundcloud.com/paulmond" title="paul mond" target="_blank" style="color: #cccccc; text-decoration: none;">paul mond</a> · 
<a href="https://soundcloud.com/paulmond/smooth-season-rnb-flip-pack" title="SMOOTH SEASON" target="_blank" style="color: #cccccc; text-decoration: none;">SMOOTH SEASON</a>
</div>
"""

# Streamlit App Layout
st.title("┬─┬ ☕︎ノ( º , ºノ)")
st.subheader("*prototype")

# Display "Song of the Day"
st.write("🔊 ****paul mond - smooth szn")

# Embed SoundCloud Player with Blue Color
st.components.v1.html(soundcloud_embed, height=166)

# Portfolio Projects Section
st.header("the notebook")
st.write(f"[soundtrap](https://www.soundtrap.com/home/creator/projects/folders/63644883)")
st.write(f"[yt](https://youtube.com/playlist?list=PL26G5xKQCDOoiWrix94v6coGvchbwQHqI&si=3m16g4CKtS21rOY6)")
st.write(f"[stats.fm](https://stats.fm/bluetoothbrownheartgarden)")

# Footer (added working link)
st.write("🔗 [Visit my full portfolio](https://bluetoothbrownheartdotmp4.streamlit.app/)")
