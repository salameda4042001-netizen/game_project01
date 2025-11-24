import streamlit as st
from engine.game_state import GameState

st.set_page_config(page_title="2D Text RPG", layout="wide")

# 전역 게임 상태
if "game" not in st.session_state:
    st.session_state.game = GameState()

game = st.session_state.game

st.title("🧭 2D Text RPG (Keyboard + Mouse Version)")

# 키보드 입력 처리
key = st.text_input("키 입력 (WASD 이동)", "")

if key.lower() == "w":
    game.player_move(0, -1)
elif key.lower() == "s":
    game.player_move(0, 1)
elif key.lower() == "a":
    game.player_move(-1, 0)
elif key.lower() == "d":
    game.player_move(1, 0)

# 마우스 클릭 이동
x = st.number_input("X 좌표로 이동", step=1)
y = st.number_input("Y 좌표로 이동", step=1)

if st.button("해당 좌표로 이동"):
    game.player_move_to(int(x), int(y))

st.subheader("📍 현재 맵")
st.text(game.render_map())

# 전투
if st.button("공격하기"):
    log = game.player_attack()
    st.write(log)

# 상태 출력
st.subheader("플레이어 상태")
st.write(game.player)

st.subheader("몬스터 상태")
for m in game.monsters:
    st.write(str(m))
