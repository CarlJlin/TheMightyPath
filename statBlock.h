#pragma once
#include "statTypes.h"

class statBlock {
	statType Attack;
	statType HP;
	statType Resistence;
	statType Mana;
	statType MagicPoints;
	statType Agility;
public :
	statBlock() {
		Attack = (statType)1u;
		HP = (statType)1u;
		Resistence = (statType)1u;
		Mana = (statType)1u;
		MagicPoints = (statType)1u;
		Agility = (statType)1u;
	}

	explicit statBlock(statType str, statType hp, statType res, statType mana, statType MP, statType agi) {
		Attack = str;
		HP = hp;
		Resistence = res;
		Mana = mana;
		MagicPoints = MP;
		Agility = agi;
	}

	statType getAD() {
		return Attack;
	}

	statType getHP() {
		return HP;
	}
};