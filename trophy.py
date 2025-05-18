import streamlit as st
from collections import defaultdict

# Define items
ITEMS = {
    # Trophies
    "Arachnid Trophy": {"Precision": 4},
    "Chainwraith Trophy": {"Wisdom": 2, "Might": 1},
    "Crowmaiden Trophy": {"Spell Power": 4},
    "Demon Trophy": {"Impact": 4},
    "Direhorn Drake Trophy": {"Dexterity": 2, "Vitality": 1},
    "Djinn Trophy": {"Intelligence": 2, "Vitality": 1},
    "Dwarf Trophy": {"Weapon Defense": 4},
    "Elf Trophy": {"Dexterity": 2, "Wisdom": 1},
    "Emberscale Drake Trophy": {"Vitality": 2, "Intelligence": 1},
    "Fox Trophy": {"Haste": 4},
    "Froll Trophy": {"Max Health": 4},
    "Frostbound Drake Trophy": {"Weapon Power": 4},
    "Frostrisen Trophy": {"Max Mana": 6},
    "Fungi Trophy": {"Healing Power": 4},
    "Gazer Trophy": {"Mana Regeneration": 4},
    "Ghaz Trophy": {"Dexterity": 2, "Wisdom": 1},
    "Goblin Trophy": {"Intelligence": 2, "Dexterity": 1},
    "Hookmask Trophy": {"Healing Power": 4},
    "Iceforge Dwarf Trophy": {"Might": 2, "Intelligence": 1},
    "Jackal Trophy": {"Spell Defense": 4},
    "Kaiman Trophy": {"Precision": 4},
    "Mindslave Trophy": {"Max Mana": 6},
    "Minotaur Trophy": {"Might": 2, "Vitality": 1},
    "Morningstar Trophy": {"Haste": 4},
    "Orc Trophy": {"Weapon Power": 4},
    "Pirate Trophy": {"Wisdom": 2, "Might": 1},
    "Pummeldillos Trophy": {"Weapon Defense": 4},
    "Rat Trophy": {"Dexterity": 2, "Intelligence": 1},
    "Rohna Brotherhood Trophy": {"Impact": 4},
    "Saltdusk Trophy": {"Vitality": 2, "Wisdom": 1},
    "Saurian Trophy": {"Intelligence": 2, "Might": 1},
    "Shark Trophy": {"Might": 2, "Dexterity": 1},
    "Skeleton Trophy": {"Max Health": 4},
    "Skorn Trophy": {"Spell Power": 4},
    "Spellslayer Drake Trophy": {"Spell Defense": 4},
    "Sporewalker Trophy": {"Max Mana": 6},
    "Toad Trophy": {"Max Health": 4},
    "Tortoise Trophy": {"Vitality": 2, "Wisdom": 1},
    "Troll Trophy": {"Health Regeneration": 4},
    "Trunk Trophy": {"Mana Regeneration": 4},
    "Vampire Trophy": {"Intelligence": 2, "Dexterity": 1},
    "Venomfang Drake Trophy": {"Health Regeneration": 4},
    "Warhog Trophy": {"Might": 2, "Vitality": 1},
    "Winterborn Trophy": {"Wisdom": 2, "Intelligence": 1},
    "Yeti Trophy": {"Vitality": 2, "Might": 1},
    "Zorian Trophy": {"Wisdom": 2, "Dexterity": 1},

    # Monuments
    "Monument to Brutality": {"Weapon Power": 4},
    "Monument to Vitality": {"Vitality": 3},
    "Monument to Might": {"Might": 3},
    "Monument to Wisdom": {"Wisdom": 3},
    "Monument to Dexterity": {"Dexterity": 3},
    "Monument to Bloodlust": {"Max Health": 4, "Health Regeneration": 4},
    "Monument to Grudges": {"Healing Power": 4},
    "Monument to Desolation": {"Spell Power": 4},
    "Monument to Subjugation": {"Spell Defense": 4},
    "Monument to Obsession": {"Weapon Defense": 4},
    "Monument to Envy": {"Haste": 4},
    "Monument to Prec": {"Precision": 1, "Impact":3},
    "Monument to Impac": {"Precision": 3, "Impact":1},
    "Monument to Ocean": {"Weapon Power": 2, "Spell Power":2},
}

# Split items by category
TROPHIES = [item for item in ITEMS if "Trophy" in item]
MONUMENTS = [item for item in ITEMS if "Monument" in item]

st.title("🏆 Trophy & Monument Bonus Calculator")

# Select all checkboxes
select_all_trophies = st.checkbox("✔️ Select All Trophies")
select_all_monuments = st.checkbox("✔️ Select All Monuments")

# Multiselect dropdowns
selected_trophies = st.multiselect(
    "Select your trophies:",
    TROPHIES,
    default=TROPHIES if select_all_trophies else []
)

selected_monuments = st.multiselect(
    "Select your monuments:",
    MONUMENTS,
    default=MONUMENTS if select_all_monuments else []
)

# Combine selected
selected_items = selected_trophies + selected_monuments

# Calculate bonuses
total_stats = defaultdict(int)
for item in selected_items:
    for stat, bonus in ITEMS[item].items():
        total_stats[stat] += bonus

# Display
st.subheader("📊 Total Bonus Summary")
if total_stats:
    for stat, bonus in sorted(total_stats.items()):
        st.write(f"**{stat}**: {bonus}%")
else:
    st.info("Select some trophies or monuments to see your cumulative bonuses.")
