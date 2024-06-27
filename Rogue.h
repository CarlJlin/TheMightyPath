#pragma once
#include "hp.h"
#include "statBlock.h"

class Rogue : public hp, public statBlock {

public:
	static const statType baseAttack = (statType)35u;
	static const statType AttackGrowth = (statType)6;
	static const hptype HPGrowth = (hptype)5u;
	static const hptype baseHP = (hptype)45u;
	static const statType baseMana = (statType)4u;
	static const statType ManaGrowth = (statType)2u;
	static const statType baseRes = (statType)20u;
	static const statType ResGrowth = (statType)2u;
	static const statType baseMP = (statType)3u;
	static const statType MPGrowth = (statType)1u;
	static const statType baseAgi = (statType)25u;
	static const statType AgiGrowth = (statType)3u;

	Rogue() : hp(baseHP, HPGrowth), statBlock(baseAttack, baseHP, baseRes, baseMana, baseMP, baseAgi) {


	};


private:


};