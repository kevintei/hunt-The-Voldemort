import random

class HuntVoldemort:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.dungeons = {i: [((i + j) % 20) + 1 for j in range(1, 4)] for i in range(1, 21)}
        self.player_position = random.randint(1, 20)
        self.voldemort_position = random.randint(1, 20)
        while self.voldemort_position == self.player_position:
            self.voldemort_position = random.randint(1, 20)
        self.trap_positions = random.sample(
            [i for i in range(1, 21) if i != self.player_position and i != self.voldemort_position],
            3
        )
        self.dementor_positions = random.sample(
            [i for i in range(1, 21) if i not in self.trap_positions and i != self.player_position and i != self.voldemort_position],
            2
        )
        self.wand_charges = 5  # Player starts with 5 Expelliarmus charges

    def print_dungeon_info(self):
        connected = self.dungeons[self.player_position]
        print(f"\nYou are in Dungeon {self.player_position}.")
        print(f"Connected dungeons: {connected}")
        if any(pos in connected for pos in self.trap_positions):
            print("You feel a dark presence nearby...")
        if self.voldemort_position in connected:
            print("You hear sinister whispers... Voldemort might be near!")
        if any(pos in connected for pos in self.dementor_positions):
            print("A cold chill runs down your spine... Dementors are near!")

    def move_player(self, dungeon):
        if dungeon in self.dungeons[self.player_position]:
            self.player_position = dungeon
            if self.player_position in self.trap_positions:
                print("You fell into a trap! Game Over!")
                return False
            elif self.player_position == self.voldemort_position:
                print("You've been caught by Voldemort! Game Over!")
                return False
            elif self.player_position in self.dementor_positions:
                print("A Dementor grabs you and whisks you away!")
                self.player_position = random.randint(1, 20)
                print(f"You are dropped in Dungeon {self.player_position}.")
                if self.player_position in self.trap_positions:
                    print("You fell into a trap! Game Over!")
                    return False
                elif self.player_position == self.voldemort_position:
                    print("You've been caught by Voldemort! Game Over!")
                    return False
                return True
            else:
                return True
        else:
            print("You can't move there! Choose a connected dungeon.")
            return True

    def cast_expelliarmus(self, dungeon):
        if self.wand_charges <= 0:
            print("You have no wand charges left! Voldemort wins!")
            return False
        self.wand_charges -= 1
        print(f"You cast Expelliarmus towards Dungeon {dungeon}.")
        if dungeon == self.voldemort_position:
            print("You hit Voldemort with Expelliarmus! You've won!")
            return False
        else:
            print("Your spell missed...")
            return True

    def play(self):
        print("Welcome to Hunt Voldemort!")
        print("You must navigate through the dungeons to defeat Voldemort.")
        print("Use your wand to cast Expelliarmus to attack him. Beware of traps and Dementors!")
        while True:
            game_on = True
            self.initialize_game()
            while game_on:
                self.print_dungeon_info()
                action = input("What will you do? (move [dungeon] / cast [dungeon]): ").strip().lower()
                if action.startswith("move"):
                    try:
                        dungeon = int(action.split()[1])
                        game_on = self.move_player(dungeon)
                    except (IndexError, ValueError):
                        print("Invalid command. Use 'move [dungeon]' to move.")
                elif action.startswith("cast"):
                    try:
                        dungeon = int(action.split()[1])
                        game_on = self.cast_expelliarmus(dungeon)
                    except (IndexError, ValueError):
                        print("Invalid command. Use 'cast [dungeon]' to attack.")
                else:
                    print("Invalid command. Use 'move' or 'cast'.")

            # Ask if the player wants to play again
            replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if replay != "yes":
                print("Mischief Managed! Goodbye!")
                break

# Run the game
if __name__ == "__main__":
    game = HuntVoldemort()
    game.play()
