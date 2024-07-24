use std::collections::HashMap;
use std::io::{self, Write};

#[derive(Debug)]
struct PasswordManager {
    passwords: HashMap<String, String>,
}

impl PasswordManager {
    fn new() -> Self {
        PasswordManager {
            passwords: HashMap::new(),
        }
    }

    fn add_password(&mut self, site: String, password: String) {
        self.passwords.insert(site, password);
    }

    fn get_password(&self, site: &str) -> Option<&String> {
        self.passwords.get(site)
    }

    fn display_all(&self) {
        for (site, password) in &self.passwords {
            println!("Site: {}, Password: {}", site, password);
        }
    }
}

fn main() {
    let mut manager = PasswordManager::new();
    loop {
        println!("Password Manager");
        println!("1. Add password");
        println!("2. Retrieve password");
        println!("3. Display all passwords");
        println!("4. Exit");

        let mut choice = String::new();
        print!("Enter your choice: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut choice).unwrap();
        let choice: u32 = choice.trim().parse().unwrap_or(0);

        match choice {
            1 => {
                let mut site = String::new();
                let mut password = String::new();
                
                print!("Enter site: ");
                io::stdout().flush().unwrap();
                io::stdin().read_line(&mut site).unwrap();
                let site = site.trim().to_string();

                print!("Enter password: ");
                io::stdout().flush().unwrap();
                io::stdin().read_line(&mut password).unwrap();
                let password = password.trim().to_string();

                manager.add_password(site, password);
                println!("Password added!");
            }
            2 => {
                let mut site = String::new();
                
                print!("Enter site to retrieve password: ");
                io::stdout().flush().unwrap();
                io::stdin().read_line(&mut site).unwrap();
                let site = site.trim();

                match manager.get_password(site) {
                    Some(password) => println!("Password for {}: {}", site, password),
                    None => println!("No password found for {}", site),
                }
            }
            3 => {
                manager.display_all();
            }
            4 => {
                println!("Exiting...");
                break;
            }
            _ => println!("Invalid choice, please try again."),
        }
    }
}
