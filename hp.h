#pragma once
//Author @CarlJlin
//File hp.h
//Project FirstGameV1

#include "hptypes.h"


class hp {
public :
	// returns true if set successfully
	bool setMaxHP(hptype new_max_hp) {
		if (new_max_hp < 1)
			return false;

		MaxHP = new_max_hp;

		if (CurrentHP > MaxHP)
			CurrentHP = MaxHP;

		return true;
	}

	void takeDamage(hptype damage) {
		if (damage > CurrentHP) {
			CurrentHP = 0;
			return;
		}
		CurrentHP -= damage;
	}

	void heal(hptype amount) {
		if (CurrentHP + amount > MaxHP) {
			CurrentHP = MaxHP;
			return;
		}

		CurrentHP += amount;
	}


	hptype getCurrentHP() {
		return CurrentHP;
	}

	hptype getMaxHP() {
		return MaxHP;
	}

	hp() {
		CurrentHP = 1;
		MaxHP = 1;
	}
	hp(hptype cHP, hptype mHP) {
		CurrentHP = cHP;
		MaxHP = mHP;
		if (CurrentHP > MaxHP)
			CurrentHP = MaxHP;
	}

private:
	hptype CurrentHP;
	hptype MaxHP;
protected:
};