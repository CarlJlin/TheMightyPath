#pragma once
#include "hp.h"
#include "statBlock.h"

class Cleric : public hp, public statBlock {

public:
	static const statType baseAttack = (statType)5u;
	static const statType AttackGrowth = (statType)1;
	static const hptype HPGrowth = (hptype)3u;
	static const hptype baseHP = (hptype)30u;
	static const statType baseMana = (statType)50u;
	static const statType ManaGrowth = (statType)6u;
	static const statType baseRes = (statType)10u;
	static const statType ResGrowth = (statType)1u;
	static const statType baseMP = (statType)40u;
	static const statType MPGrowth = (statType)5u;
	static const statType baseAgi = (statType)5u;
	static const statType AgiGrowth = (statType)1.5;

	Cleric() : hp(baseHP, HPGrowth), statBlock(baseAttack, baseHP, baseRes, baseMana, baseMP, baseAgi) {


	};


private:


};
