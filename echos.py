import streamlit as st
import json
import os
import random

DATA_FILE = "players_simple.json"

# Load and save functions
# Load and validate data
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                if isinstance(data, list) and all(isinstance(p, dict) and "name" in p for p in data):
                    return data
        except Exception as e:
            print("Data load failed:", e)
    # Return empty if data invalid or load fails
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Initialization with cleanup
if "players" not in st.session_state:
    clean_data = load_data()
    st.session_state.players = clean_data
    if clean_data != []:
        save_data(clean_data)  # Overwrite any malformed file

st.title("🌀 Aether Echo Party Scheduler")

st.header("➕ Add Yourself")
with st.form("add_player_form"):
    name = st.text_input("Name")
    role = st.selectbox("Role", ["DPS", "Tank", "Healer"])
    has_easy = st.checkbox("Has Easy Scroll")
    has_medium = st.checkbox("Has Medium Scroll")
    is_ready = st.checkbox("Ready to Echo")
    submitted = st.form_submit_button("Add Player")

    if submitted:
        if name and all(p["name"] != name for p in st.session_state.players):
            st.session_state.players.append({
                "name": name,
                "role": role,
                "easy": has_easy,
                "medium": has_medium,
                "ready": is_ready
            })
            save_data(st.session_state.players)
            st.success(f"{name} added!")
        elif not name:
            st.error("Please enter a name.")
        else:
            st.warning("Name already exists.")

st.markdown("---")
st.header("✅ Ready Players")

ready_players = [p for p in st.session_state.players if p["ready"]]
if not ready_players:
    st.info("No players marked as ready.")
else:
    for p in ready_players:
        st.markdown(
            f"- **{p['name']}** ({p['role']}) | "
            f"Easy: {'✅' if p['easy'] else '❌'} | "
            f"Medium: {'✅' if p['medium'] else '❌'}"
        )

st.markdown("---")
st.header("🎯 Generate Parties")

if st.button("🧩 Generate Ideal Parties"):
    dps = [p for p in ready_players if p["role"] == "DPS"]
    tanks = [p for p in ready_players if p["role"] == "Tank"]
    healers = [p for p in ready_players if p["role"] == "Healer"]

    random.shuffle(dps)
    random.shuffle(tanks)
    random.shuffle(healers)

    num_parties = min(len(dps) // 2, len(tanks), len(healers))
    st.success(f"Generated {num_parties} party(ies):")

    used_names = set()
    for i in range(num_parties):
        party_dps = dps[i*2:(i*2)+2]
        party_tank = tanks[i]
        party_healer = healers[i]
        party = party_dps + [party_tank, party_healer]

        st.markdown(f"### 🛡️ Party {i + 1}")
        for p in party:
            used_names.add(p["name"])
            st.markdown(f"- **{p['name']}** ({p['role']}) | Easy: {'✅' if p['easy'] else '❌'}, Medium: {'✅' if p['medium'] else '❌'}")

    leftovers = [p for p in ready_players if p["name"] not in used_names]
    if leftovers:
        st.markdown("### ❗ Leftover Ready Players")
        for p in leftovers:
            st.markdown(f"- {p['name']} ({p['role']})")

st.markdown("---")
if st.button("🧹 Reset All Players"):
    st.session_state.players = []
    save_data([])
    st.experimental_rerun()
