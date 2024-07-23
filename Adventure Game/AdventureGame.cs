using System;

namespace TextAdventureGame
{
    class Program
    {
        static void Main(string[] args)
        {
            Game game = new Game();
            game.Start();
        }
    }

    class Game
    {
        Player player;

        public void Start()
        {
            player = new Player();

            Console.WriteLine("Welcome to the Text Adventure Game!");
            Console.Write("Enter your name: ");
            player.Name = Console.ReadLine();

            Console.WriteLine($"Hello, {player.Name}! Your adventure begins now.");
            FirstScenario();
        }

        void FirstScenario()
        {
            Console.WriteLine("You find yourself in a dark forest. There are two paths ahead.");
            Console.WriteLine("1. Take the left path.");
            Console.WriteLine("2. Take the right path.");
            Console.Write("What do you want to do? ");

            string choice = Console.ReadLine();

            if (choice == "1")
            {
                LeftPath();
            }
            else if (choice == "2")
            {
                RightPath();
            }
            else
            {
                Console.WriteLine("Invalid choice. Try again.");
                FirstScenario();
            }
        }

        void LeftPath()
        {
            Console.WriteLine("You took the left path and encountered a wild animal!");
            Console.WriteLine("1. Fight the animal.");
            Console.WriteLine("2. Run away.");
            Console.Write("What do you want to do? ");

            string choice = Console.ReadLine();

            if (choice == "1")
            {
                FightAnimal();
            }
            else if (choice == "2")
            {
                Console.WriteLine("You ran away safely but got lost.");
                FirstScenario();
            }
            else
            {
                Console.WriteLine("Invalid choice. Try again.");
                LeftPath();
            }
        }

        void RightPath()
        {
            Console.WriteLine("You took the right path and found a treasure chest!");
            Console.WriteLine("1. Open the chest.");
            Console.WriteLine("2. Ignore the chest and move on.");
            Console.Write("What do you want to do? ");

            string choice = Console.ReadLine();

            if (choice == "1")
            {
                OpenChest();
            }
            else if (choice == "2")
            {
                Console.WriteLine("You ignored the chest and moved on.");
                Console.WriteLine("Your adventure continues...");
            }
            else
            {
                Console.WriteLine("Invalid choice. Try again.");
                RightPath();
            }
        }

        void FightAnimal()
        {
            Random random = new Random();
            int outcome = random.Next(0, 2); // Randomly determine the outcome (0 or 1)

            if (outcome == 0)
            {
                Console.WriteLine("You fought bravely but the animal overpowered you. Game over.");
            }
            else
            {
                Console.WriteLine("You defeated the animal and continued on your path.");
                FirstScenario();
            }
        }

        void OpenChest()
        {
            Random random = new Random();
            int outcome = random.Next(0, 2); // Randomly determine the outcome (0 or 1)

            if (outcome == 0)
            {
                Console.WriteLine("The chest was empty. Better luck next time.");
            }
            else
            {
                Console.WriteLine("You found gold and precious gems! You're rich!");
            }
        }
    }

    class Player
    {
        public string Name { get; set; }
    }
}
