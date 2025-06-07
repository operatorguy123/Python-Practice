import random

# Base Character Class
class RPG:
    def __init__(self, name, health, max_health, attack_power, defense, speed, crit_chance, attack_name):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
        self.crit_chance = crit_chance  # between 0.0 and 1.0
        self.attack_name = attack_name

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        print(f"{self.name} takes {amount} damage. HP: {self.health}/{self.max_health}")

    def attack(self, opponent):
        damage = max(1, self.attack_power - opponent.defense)
        if random.random() < self.crit_chance:
            damage *= 2
            print(f"💥 Critical hit!")
        print(f"{self.name} uses {self.attack_name} on {opponent.name}!")
        opponent.take_damage(damage)

# Item Class
class Item:
    def __init__(self, name, item_type, power, description):
        self.name = name
        self.type = item_type  # "heal", "buff", "debuff"
        self.power = power
        self.description = description

# Player Class
class Player(RPG):
    def __init__(self, name, health, max_health, attack_power, defense, speed, crit_chance, attack_name):
        super().__init__(name, health, max_health, attack_power, defense, speed, crit_chance, attack_name)
        self.inventory = {}
        self.max_inventory = 5

    def add_item(self, item):
        total_items = sum(self.inventory.values())
        if total_items >= self.max_inventory:
            print("🧺 Inventory full!")
            return False
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1
        return True

    def use_item(self, item, target=None):
        print(f"{self.name} uses {item.name}: {item.description}")
        if item.type == "heal":
            self.health = min(self.max_health, self.health + item.power)
            print(f"{self.name} heals for {item.power}. HP: {self.health}/{self.max_health}")
        elif item.type == "buff":
            self.attack_power += item.power
            print(f"{self.name}'s attack increased by {item.power}.")
        elif item.type == "debuff" and target:
            target.attack_power = max(0, target.attack_power - item.power)
            print(f"{target.name}'s attack power reduced by {item.power}.")
        self.inventory[item] -= 1
        if self.inventory[item] == 0:
            del self.inventory[item]

# Enemy Class
class Enemy(RPG):
    def __init__(self, name, health, max_health, attack_power, defense, speed, crit_chance, attack_name):
        super().__init__(name, health, max_health, attack_power, defense, speed, crit_chance, attack_name)

# Sample Items
potion = Item("Potion", "heal", 30, "Restores 30 HP")
elixir = Item("Elixir", "buff", 5, "Increases attack power by 5")
curse_scroll = Item("Curse Scroll", "debuff", 4, "Reduces enemy's attack power by 4")

# Create Players
knight = Player("Knight", 120, 120, 20, 10, 5, 0.1, "Holy Slash")
rogue = Player("Rogue", 90, 90, 18, 5, 10, 0.3, "Backstab")
mage = Player("Mage", 80, 80, 25, 3, 6, 0.2, "Firebolt")

# Add Items
for p in [knight, rogue, mage]:
    p.add_item(potion)
    p.add_item(potion)
    p.add_item(elixir)
    p.add_item(curse_scroll)

# Choose Player
players = [knight, rogue, mage]
print("Choose your character:")
for i, p in enumerate(players, 1):
    print(f"{i}. {p.name}")
choice = int(input("> ")) - 1
player = players[choice]

# Create Enemies
goblin = Enemy("Goblin", 70, 70, 15, 5, 9, 0.1, "Claw Swipe")
orc = Enemy("Orc", 130, 130, 22, 12, 4, 0.05, "Brutal Smash")
dark_mage = Enemy("Dark Mage", 60, 60, 30, 4, 6, 0.2, "Dark Blast")

enemies = [goblin, orc, dark_mage]
enemy = random.choice(enemies)
print(f"\n⚔️ Battle Start: {player.name} vs {enemy.name}!\n")

# Battle Loop
turn = 1
while player.is_alive() and enemy.is_alive():
    print(f"\n🔄 Turn {turn}")
    print(f"{player.name}: {player.health}/{player.max_health} HP | {enemy.name}: {enemy.health}/{enemy.max_health} HP")

    participants = sorted([player, enemy], key=lambda c: c.speed, reverse=True)

    for combatant in participants:
        if not player.is_alive() or not enemy.is_alive():
            break

        if combatant == player:
            print("Choose an action:")
            print("1. Attack")
            print("2. Use Item")
            action = input("> ")

            if action == "1":
                player.attack(enemy)
            elif action == "2":
                if not player.inventory:
                    print("📦 No items left.")
                    continue
                print("Inventory:")
                for i, (item, count) in enumerate(player.inventory.items(), 1):
                    print(f"{i}. {item.name} x{count} - {item.description}")
                try:
                    idx = int(input("Select item: ")) - 1
                    item_list = list(player.inventory.keys())
                    if 0 <= idx < len(item_list):
                        item = item_list[idx]
                        if item.type == "debuff":
                            player.use_item(item, target=enemy)
                        else:
                            player.use_item(item)
                    else:
                        print("❌ Invalid selection.")
                        continue
                except:
                    print("❌ Invalid input.")
                    continue
            else:
                print("❌ Invalid action.")
        else:
            if enemy.is_alive():
                enemy.attack(player)

    print("-" * 40)
    turn += 1


# Outcome
if player.is_alive():
    print(f"\n🎉 {player.name} wins against the {enemy.name}!")
else:
    print(f"\n💀 {player.name} was defeated by the {enemy.name}...")
