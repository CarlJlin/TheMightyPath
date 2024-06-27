//Author @CarlJlin
//File main.cpp
//Project FirstGameV1

#include <iostream>
#include "Knight.h"
#include "Mage.h"
#include "Cleric.h"
#include "Rogue.h"

int main() {
	Knight knight1;
	Mage mage1;
	Cleric cleric1;
	Rogue rogue1;

	std::cout << "Knight\n" << "- HP: " << knight1.getHP() << "\n- Attack: "
		<< knight1.getAD() << '\n';
	std::cout << "Mage\n" << "- HP: " << mage1.getHP() << "\n- Attack: "
		<< mage1.getAD() << '\n';
	std::cout << "Cleric\n" << "- HP: " << cleric1.getHP() << "\n- Attack: "
		<< cleric1.getAD() << '\n';
	std::cout << "Rogue\n" << "- HP: " << rogue1.getHP() << "\n- Attack: "
		<< rogue1.getAD() << '\n';

	while (true) {

	}
}